import psycopg2
import json

BomJson =[]
with open('BomJson.json') as file:
    BomJson = json.load(file)

print(BomJson)

connection = psycopg2.connect(
    dbname = "bom_vector",
    user = "postgres",
    password = "",
    host = "localhost",
    port = "5432"
)