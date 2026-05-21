### Build a Question Answering Application over a Graph Database
import os 
from dotenv import load_dotenv
load_dotenv()
NEO4J_URI = os.environ['NEO4J_URI'] 
NEO4J_USERNAME = os.environ['NEO4J_USERNAME']
NEO4J_PASSWORD = os.environ['NEO4J_PASSWORD']
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)

with driver.session(database="system") as session:
    result = session.run("SHOW DATABASES")
    for record in result:
        print(record)
from langchain_community.graphs import Neo4jGraph
graph = Neo4jGraph(url=NEO4J_URI,username=NEO4J_USERNAME,password=NEO4J_PASSWORD,database="6f624111")
graph
## Dataset Moview 
moview_query="""
LOAD CSV WITH HEADERS FROM
'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv' as row

MERGE(m:Movie{id:row.movieId})
SET m.released = date(row.released),
    m.title = row.title,
    m.imdbRating = toFloat(row.imdbRating)
FOREACH (director in split(row.director, '|') | 
    MERGE (p:Person {name:trim(director)})
    MERGE (p)-[:DIRECTED]->(m))
FOREACH (actor in split(row.actors, '|') | 
    MERGE (p:Person {name:trim(actor)})
    MERGE (p)-[:ACTED_IN]->(m))
FOREACH (genre in split(row.genres, '|') | 
    MERGE (g:Genre {name:trim(genre)})
    MERGE (m)-[:IN_GENRE]->(g))

"""
moview_query
graph.query(moview_query)
graph.refresh_schema()
print(graph.schema)
import os 
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm = ChatGroq(api_key=groq_api_key,model='llama-3.3-70b-versatile')
llm
from langchain_classic.chains import GraphCypherQAChain
chain = GraphCypherQAChain.from_llm(graph=graph,llm=llm,verbose = True,allow_dangerous_requests= True)
chain
response = chain.invoke({'query':'Who was the director of the movie Casino'})
response
response = chain.invoke({'query':'Who were the actors of the movie Casino '})
response
response = chain.invoke({'query':'Tell me about Robert De Niro'})
response
response = chain.invoke({'query':'Tell me about Quentin Tarantino, in which movie he acted in'})
response
