import json
import os 
import sys
import boto3
import streamlit as st

# we will be using titan embeddings model for to generate embeddings

from langchain_aws import BedrockEmbeddings
from langchain_aws import ChatBedrock, BedrockLLM

## DataIngestion

import numpy as np 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

## Vector Embedding and Vector Store 

from langchain_community.vectorstores import FAISS 

## LLM Models 
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA

## Bedrock client 

bedrock = boto3.client(service_name = 'bedrock-runtime',region_name = 'us-east-1')
bedrock_embedding = BedrockEmbeddings(model_id = 'amazon.titan-embed-text-v1',client=bedrock)

## DataIngestion

def data_ingestion():
    loader = PyPDFDirectoryLoader('data')
    documents = loader.load()

    # In our testing recursive character text splitter works better with this PDF dataset
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000,
                                                   chunk_overlap = 1000)
    
    docs = text_splitter.split_documents(documents)
    return docs 

# Vector Embeddings and vector store 

def get_vector_store(docs):
    vector_store_faiss = FAISS.from_documents(
        docs,
        bedrock_embedding
    )
    vector_store_faiss.save_local("faiss_index")


def get_llama_model():
    llm = BedrockLLM(
        model_id="meta.llama3-8b-instruct-v1:0",
        client=bedrock,
        model_kwargs={
            "max_gen_len": 512,
            "temperature": 0.5,
            "top_p": 0.9
        }
    )
    return llm


prompt_template = """

Human: Use the following pieces of context to provide a 
concise answer to the question at the end but use atleast summarize with 
250 words with detailed explaantions. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context>

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


def get_response_llm(llm,vector_store_faiss,query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store_faiss.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
    answer=qa({"query":query})
    return answer['result']


def main():
    st.set_page_config("Chat PDF")
    
    st.header("Chat with PDF using AWS Bedrock💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    with st.sidebar:
        st.title("Update Or Create Vector Store:")
        
        if st.button("Vectors Update"):
            with st.spinner("Processing..."):
                docs = data_ingestion()
                get_vector_store(docs)
                st.success("Done")


    if st.button("Llama3 Output"):
        with st.spinner("Processing..."):
            faiss_index = FAISS.load_local("faiss_index", bedrock_embedding,allow_dangerous_deserialization=True)
            llm=get_llama_model()
            
            #faiss_index = get_vector_store(docs)
            st.write(get_response_llm(llm,faiss_index,user_question))
            st.success("Done")

if __name__ == "__main__":
    main()
