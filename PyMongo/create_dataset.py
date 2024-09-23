import dateutil.parser
import pymongo
from faker import Faker
import random
import string
import datetime

fake = Faker()

client = pymongo.MongoClient("mongodb+srv://jonathansatria16:jovande16@cluster0.2pnpdog.mongodb.net/")
db = client["db_kapita"]
collection = db["students_collection"]

def create_dummy_user():
    digits = string.digits
    random_number_string = '24' + ''.join(random.choice(digits) for _ in range(8))
    
    return {
        "_id": random_number_string,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "birthdate": dateutil.parser.parse(fake.date_time_between_dates(datetime.datetime(2003, 1, 1), datetime.datetime(2005, 12, 31)).strftime('%Y-%m-%d')),
        "registered_at": dateutil.parser.parse(fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'))
    }

for _ in range(20):
    user_data = create_dummy_user()
    collection.insert_one(user_data)
    print("20 dummy users have been successfully inserted into the collection.")


