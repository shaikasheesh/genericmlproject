import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #decorater
class DataIngestionConfig:
    train_path: str = os.path.join('artifacts',"train.csv") #get output of train data in artifacts folder
    test_path: str = os.path.join('artifacts',"test.csv")
    rawdata_path: str = os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingetion") #logging the information
        try:
            df = pd.read_csv('data\stud.csv') #reading the dataset
            logging.info("data is read")
            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok = True)
            df.to_csv(self.ingestion_config.rawdata_path,index = False, header = True)

            logging.info('train test split initiated')
            train_set,test_set = train_test_split(df,test_size = 0.2,random_state = 42)
            train_set.to_csv(self.ingestion_config.train_path,index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_path,index = False, header = True)
            logging.info("ingestion is completed")
            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
            
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
