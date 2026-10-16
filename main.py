from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPiplineConfig

from networksecurity.logging.logger import logging

import sys

if __name__ == '__main__':
    try:
        trainingpiplineconfig = TrainingPiplineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpiplineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info('Initiate the data ingestion')
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as  e:
        raise NetworkSecurityException(e,sys)