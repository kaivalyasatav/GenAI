import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_classic.chains import LLMMathChain, LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents import Tool, initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from dotenv import load_dotenv

# Set up the streamlit app

st.set_page_config(page_title="Text to Math Problem Solver And Data Search Assistant",page_icon='🧮')
st.title("Text to Math Problem Solver")

openai_api_key = st.sidebar.text_input(label="OpenAI API Key",type="password")

if not openai_api_key:
    st.info("Please add your OpenAI API Key to Continue")
    st.stop()

llm = ChatOpenAI(model='gpt-4',api_key = openai_api_key)

# Initializing the tools

wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name = "Wikipedia",
    func = wikipedia_wrapper.run,
    description = "A tool for searching the internet to find the various information on the topics mentioned"
)

# Initialize the map tool

math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name = 'Calculator',
    func = math_chain.run,
    description = 'A tool for answering math related questions. Only input mathematical expressions needs to be provided'
)

prompt = """
You are a agent tasked for solving users mathematical questions.Logically arrive at the solution and provide a detailed explanation
and display it point-wise for the question below
Question:{question}
Answer:
"""
prompt_template = PromptTemplate(
    input_variables=['question'],
    template=prompt
)

## Combine all the tools into chain

chain = LLMChain(llm=llm,prompt = prompt_template)

reasoning_tool = Tool(
    name = 'Reasoning Tool',
    func = chain.run,
    description = 'A tool for answering logic-based and reasoning questions.'
)

# initialize the agents

assistant_agent = initialize_agent(
    tools = [wikipedia_tool,calculator,reasoning_tool],
    llm = llm,
    verbose = False,
    handle_parsing_errors = True
)

if 'messages' not in st.session_state:
    st.session_state['messages']=[
        {"role":'assistant','content':'I am a Math ChatBot who can answer all your math queries'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])


## Function to generate the response

def generate_response(question):
    response = assistant_agent.invoke({'input':question})
    return response 

# Lets start the interaction

question=st.text_area("Enter your question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end? ")

if st.button("Find my answer"):
    if question:
        with st.spinner("Generate response..."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message('user').write(question)

            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts = False)
            response = assistant_agent.run(st.session_state.messages,callbacks = [st_cb])
            st.session_state.messages.append({'role':'assistant','content':response})
            st.write('### Response:')
            st.success(response)
    else:
        st.warning("Please enter a question")