import ollama
import psycopg2
import json

async def InsertQuery(connection, BomJson):
    insert_statement = """INSERT INTO embedded_docs (verse_title, given_vector, doc_page) VALUES (%s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS embedded_docs")
    cursor.execute("""
    CREATE TABLE embedded_docs (
        id SERIAL PRIMARY KEY,
        verse_title TEXT,
        given_vector FLOAT8[],
        doc_page TEXT
    )
""")
    for i, item in enumerate(BomJson):
            title = item["Title"]
            text = item["Text"]
            vectors = get_embedding(item["Text"])
            print("This works")
            await cursor.execute(insert_statement, (title, text, vectors))
    connection.commit()
    cursor.close()
    connection.close()

def get_embedding(text_list):
    embedding_list = []
    vectors = ollama.embeddings(model=embedder_model, prompt= text_list)
    embedding_list.append(vectors)
    return embedding_list

"""
Main Code
"""

embedder_model = "nomic-embed-text"
BomJson =[]
pg_connection = psycopg2.connect(
    dbname = "bom_vector",
    user = "postgres",
    password = "FireN@tion1",
    host = "localhost",
    port = "5432"
)

with open('BomJson.json') as file:
    BomJson = json.load(file)

vector_embeddings = get_embedding(BomJson)
InsertQuery(pg_connection, vector_embeddings)