from pymongo.mongo_client import MongoClient
import datetime
URI = "mongodb+srv://jonathansatria16:jovande16@cluster0.2pnpdog.mongodb.net/"

client = MongoClient(URI)

db = client['db_kapita']

collection = db['students_collection']

# document = collection.find({'first_name': 'Anthony'})
# print(list(document))
# for doc in document:
#     print(doc)

#Insert
# documents = {
#     '_id': '124124124',
#     'first_name': 'Anthony',
#     'last_name': 'Satria',
#     'age': 20,
#     'address': 'Jl. Kebon Jeruk Raya No. 1',
#     'phone_number': '08123456789',
#     'email': 'anthonyz@gmail.com',
#     'birthdate': datetime.datetime(2001,1,1),
#     'registered_at': datetime.datetime(2024,5,22,3,14,1)
# }
# collection.insert_one(documents)

#InsertMany
documents = [
    {
        "_id": "222221",
        "first_name": "Budhi",
        "last_name": "Maharani",
        "email": "fionabudhi1231d2s@example.org",
        "address": "64113 Nowhere",
        "phone_number": "08509876543",
        "birthdate": datetime.datetime(2003, 1, 1),
        "registered_at": datetime.datetime(2024, 5, 22, 3, 14, 1)
    },
    {
        "_id": "1001212",
        "first_name": "Fiona",
        "last_name": "Maharani",
        "email": "fionaasdawdawd@example.org",
        "address": "64113 Nowhere",
        "phone_number": "08809876543",
        "birthdate": datetime.datetime(2003, 1, 1),
        "registered_at": datetime.datetime(2024, 5, 22, 3, 14, 1)
    }
]
collection.insert_many(documents)

#Update
# filter = {'_id': '2430378606'}
# value = {'$set': {'phone_number':'+69696969'}}
# result = collection.update_one(filter, value)
# print(result.modified_count)

#Update Many
# filter = {'first_name': 'Anthony'}
# value = {'$set':{'last_name': 'Jones'}}
# result = collection.update_many(filter,value)
# print(result.modified_count)

#Delete
# filter = {'_id': '2485511245'}
# result = collection.delete_one(filter)
# print(result.deleted_count)

#Delete Many
# filter = {'first_name': 'Anthony'}
# result = collection.delete_many(filter)
# print(result.deleted_count)



