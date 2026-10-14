## Data Ingestion
from datetime import datetime
import os 
from networksecurity.constant import training_pipline

print(training_pipline.PIPLINE_NAME)
print(training_pipline.ARTIFACT_DIR)


"""
Strftime :  
        Working with dates and times in Python often requires formatting them into readable strings. 
        Python provides the strftime() function lets us convert a datetime object into a formatted string using special format codes. 
        These format codes represent different parts of the date and time-like year, month, weekday, hour, etc
    """


class TrainingPiplineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipline_name = training_pipline.PIPLINE_NAME
        self.artifact_name = training_pipline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        self.timestamp : str = timestamp

class DataIngestionConfig:
    def __init__(self,training_pipline_config:TrainingPiplineConfig): ## we pass TrainingPiplineConfig obj as permter so we can acces this class  attribute 
        self.data_ingestion_dir:str  = os.path.join(
            training_pipline_config.artifact_dir,training_pipline.DATA_INGESTION_DIR_NAME
        )## ingested dir where train and test data going to store 
        ## feature store data path
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,training_pipline.DATA_INGESTION__FEATURE_STORE_DIR,training_pipline.FILE_NAME
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,training_pipline.DATA_INGESTION_INGESTED_DIR,training_pipline.TRAIN_FILE_NAME
        )
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,training_pipline.DATA_INGESTION_INGESTED_DIR,training_pipline.TEST_FILE_NAME
        )
        self.train_test_split_ratio : float = training_pipline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name : str = training_pipline.DATA_INGESTION_COLLECTION_NAME
        self.database_name :str = training_pipline.DATA_INGESTION_DATABASE_NAME
        
        