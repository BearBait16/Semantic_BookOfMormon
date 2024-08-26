import ollama
import psycopg2
import json

BomJson =[]
with open('BomJson.json') as file:
    BomJson = json.load(file)

connection = psycopg2.connect(
    dbname = "bom_vector",
    user = "postgres",
    password = "",
    host = "localhost",
    port = "5432"
)

embedder_model = "nomic-embed-text"

def get_embedding(text_list):
    embedding_list = []
    vectors = ollama.embeddings(model=embedder_model, prompt= text_list)
    embedding_list.append(vectors)
    return embedding_list

async def main():
    insert_statement = """INSERT INTO embedded_docs (verse_title, text, embedding) VALUES (%s, %s, %s)"""

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
    try:
        for i, item in enumerate(BomJson):
                title = item["Title"]
                text = item["Text"]
                vectors = get_embedding(item["Text"])
                await cursor.execute(insert_statement, (title, text, vectors))
        connection.commit()
    finally:
        cursor.close()
        connection.close()