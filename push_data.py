import os 
import sys 
import certifi
import json
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL_KEY")
print(MONGO_DB_URL)


# certifi -> certifi is used for checking a given request is certified or not means secure or not when we try to assosate with mongodb

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e :
             raise NetworkSecurityException(e,sys)
    
    def cv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads((data.T.to_json())).values()) # convert this data into json and then add this data into mogodb
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_clients = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_clients[self.database] # we tell mongo which dataset we are using 
            self.collection = self.database[self.collection] # we tell mongo what collection we are using in database
            self.collection.insert_many(self.records)
            
            return(len(self.records))
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
        
if __name__ == "__main__":
    file_path = 'Netwrok_Data/phisingData.csv'
    DATABASE =  'ARMAN'
    collection = "NetworkData"
    networkobj =  NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(file_path=file_path)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,collection)
    logging.info('DATABASE CONNECTED AND ADD RECORDS IN DATABASE DONE !!!!!!!')
    print(no_of_records)