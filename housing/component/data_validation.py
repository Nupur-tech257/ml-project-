from housing.exception import HousingException
from housing.logger import logging
import pandas as pd
import numpy as np 
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.artifact_entity import DataValidationArtifact
import os,sys
from housing.util.util import read_yaml_file
from housing.constants import *
import evidently
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json

class DataValidation :

    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def get_train_test_df (self):
        try:
            train_df= pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def does_train_test_file_exists(self)->bool:
        try:
            logging.info("checking if test and train file exists")
            train_exists=False
            test_exists=False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            train_exists=os.path.exists(train_file_path)
            test_exists=os.path.exists(test_file_path)

            is_available=train_exists and test_exists

            if not is_available:
                training_file_path= self.data_ingestion_artifact.train_file_path
                testing_file_path=self.data_ingestion_artifact.test_file_path
                logging.info(f"training file {training_file_path} and testing file {testing_file_path} are not available")
            else:
                return is_available
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def validate_dataset_schema(self):
        try:
            validation=False
            train_df,test_df=self.get_train_test_df()
            schema_file_path=SCHEMA_FILE_PATH
            schema_file=read_yaml_file(schema_file_path)

            def number_of_col():
                try:
                    if len(train_df.columns)!=len([i for i in schema_file["columns"]]):
                        msg=f"number of columns in train is not equal to number of columns in schema file "
                        raise Exception(msg)
                    elif len(test_df.columns)!=len([i for i in schema_file["columns"]]):
                        msg=f"number of columns in test is not equal to number of columns in schema file "
                        raise Exception(msg)
                    else:
                        logging.info(f"number of columns of train and test dataset are valid")
                        return True
                except Exception as e:
                    raise HousingException(e,sys) from e     
                
            def col_names():
                try:
                    if number_of_col()==True:
                        for i in train_df.columns:
                            if i not in [i for i in schema_file["columns"]]:
                                msg=f"column name in train dataset {i} is not available in schemafile "
                                raise Exception(msg)
                            else:
                                continue
                        for i in test_df.columns:
                            if i not in [i for i in schema_file["columns"]]:
                                msg=f"column name in test dataset {i} is not available in schemafile "
                                raise Exception(msg)
                            else:
                                continue   
                        return True
                except Exception as e:
                    raise HousingException(e,sys) from e
                
            def acceptable_values_in_ocean_proximity():
                try:
                    for i in train_df["ocean_proximity"].unique():
                        if i not in schema_file["domain_value"]['ocean_proximity']:
                            msg=f"{i} not acceptable value"
                            raise Exception(msg)
                        else:
                            continue
                    for i in test_df["ocean_proximity"].unique():
                        if i not in schema_file["domain_value"]['ocean_proximity']:
                            msg=f"{i} not acceptable value"
                            raise Exception(msg)
                        else:
                            continue
                    return True    
                except Exception as e:
                    raise HousingException(e,sys) from e
                 
            validation=col_names() and acceptable_values_in_ocean_proximity()

            if not validation:
                logging.info("training and testing dataframes are not valid")
            
            else:
                logging.info("training and testing dataframes are validate")
                return validation
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def get_and_save_datadrift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df,test_df = self.get_train_test_df()

            profile.calculate(train_df,test_df)

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def save_datadrift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def is_datadrift_found(self):
        try:
            report = self.get_and_save_datadrift_report()
            self.save_datadrift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def initiate_data_validation(self):
        try:
            self.does_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_datadrift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successully."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e