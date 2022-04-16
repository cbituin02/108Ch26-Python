import pymongo
import certifi


mongo_url = "mongodb+srv://FSDI:FSDICH26@cluster0.pekge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("StarStickers")
