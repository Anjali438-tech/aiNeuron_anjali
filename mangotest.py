import pymongo
import urllib
z = "mongodb+srv://patna:" + urllib.parse.quote_plus("Bittu@3018") + "@cluster0.on8bm.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(z)
db = client.test
print(db)
d= {
    "name": "anjali" ,
    "email": "anjali@gmail.com ",
    "surname" : "kumari"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)




