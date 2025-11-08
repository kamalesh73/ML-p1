import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #it stores the above paths

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(os.path.join('notebook', 'data', 'stud.csv'))  # we are reading the dataset from any source
            logging.info("Read the dataset as data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #converting the raw data into the csv file

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42) # do the train test split of the raw data

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) # train data in the csv form
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)# test data in the csv form

            logging.info("Ingestion of the data is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
              # Here we are returning the train and test to the next part of the code
            )
        except Exception as e:
            raise CustomException(e,sys)
            
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()



