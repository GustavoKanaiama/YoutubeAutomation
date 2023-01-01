from pymongo import MongoClient
client = MongoClient("mongodb+srv://ytautomation:aramefarpado@ytautomation.64lmq6e.mongodb.net/?retryWrites=true&w=majority")
print("Connection Successful")

db = client["teste"]
collection = db["testando"]
doc = {"nome": "Jeferson Caminhões", "idade": 69, "cidade": "Belfort Roxo"}
collection.insert_one(doc)


client.close()


