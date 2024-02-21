from housing.exception import HousingException
from housing.logger import logging
import os,sys
from housing.util.util import read_yaml_file
from housing.util.util import load_object
import pandas as pd
import numpy as np
from housing.constants import*


def get_latest_preprocessor_file_path():
    try:
        path=os.path.join(ROOT_DIR,HOUSING,FOLDERNAME1,DATA_TRANSFORMATION)
        dir=max(os.listdir(path))
        preprocessor_path=os.path.join(path,dir,DATA_TRANSFORMATION_FILENAME,DATA_TRANSFORMATION_PKLFILENAME)
        return preprocessor_path
    except Exception as e:
            raise HousingException(e,sys)

class Predictpipeline:
    def __init__(self,model_eval_file_path:str=MODEL_EVAL_FILE_PATH):
        try:
            self.model_eval_info=read_yaml_file(file_path=model_eval_file_path)
        except Exception as e:
            raise HousingException(e,sys)
    
    def predict(self,features):
        try:
            best_model=self.model_eval_info[BEST_MODEL]
            model_path=best_model[MODEL_PATH]
            preprocessor_path=get_latest_preprocessor_file_path()
            print("Before Loading")
            model=load_object(file_path=model_path)
            print("After Loading")
            preds=model.predict(features)
            print(preds)
            return preds
        
        except Exception as e:
            raise HousingException(e,sys)


class HousingData:

    def __init__(self,
                 longitude: float,
                 latitude: float,
                 housing_median_age: float,
                 total_rooms: float,
                 total_bedrooms: float,
                 population: float,
                 households: float,
                 median_income: float,
                 ocean_proximity: str,
                 median_house_value: float = None
                 ):
        try:
            self.longitude = longitude
            self.latitude = latitude
            self.housing_median_age = housing_median_age
            self.total_rooms = total_rooms
            self.total_bedrooms = total_bedrooms
            self.population = population
            self.households = households
            self.median_income = median_income
            self.ocean_proximity = ocean_proximity
            self.median_house_value = median_house_value
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_housing_input_data_frame(self):

        try:
            housing_input_dict = self.get_housing_data_as_dict()
            return pd.DataFrame(housing_input_dict)
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_housing_data_as_dict(self):
        try:
            input_data = {
                "longitude": [self.longitude],
                "latitude": [self.latitude],
                "housing_median_age": [self.housing_median_age],
                "total_rooms": [self.total_rooms],
                "total_bedrooms": [self.total_bedrooms],
                "population": [self.population],
                "households": [self.households],
                "median_income": [self.median_income],
                "ocean_proximity": [self.ocean_proximity]}
            return input_data
        except Exception as e:
            raise HousingException(e, sys)