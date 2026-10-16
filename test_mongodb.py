
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os 
import sys
from networksecurity.exception.exception import NetworkSecurityException

load_dotenv()
try :
    url = os.getenv('MONGO_DB_URL_KEY')
    print(url)
except Exception as e:
    raise NetworkSecurityException(e,sys)



# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    
## use use this below code for checking your database exist or not 
db_names = client.list_database_names()

for db in enumerate(db_names):
    print(f'Databases :  {db}')