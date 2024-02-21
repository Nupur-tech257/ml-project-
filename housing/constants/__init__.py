import os 
from datetime import datetime
 
ROOT_DIR= os.getcwd()
FOLDERNAME = "config"
FILENAME="config.yaml"
FILENAME_SCHEMA="schema.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,FOLDERNAME,FILENAME)
SCHEMA_FILE_PATH=os.path.join(ROOT_DIR,FOLDERNAME,FILENAME_SCHEMA)

FOLDERNAME1= "artifact"
FILENAME1="model_evaluation"
YAMLFILE="model_evaluation.yaml"
DATA_TRANSFORMATION="data transformation"
DATA_TRANSFORMATION_FILENAME="preprocessed"
DATA_TRANSFORMATION_PKLFILENAME="preprocessed.pkl"
HOUSING="housing"
MODEL_EVAL_FILE_PATH=os.path.join(ROOT_DIR,HOUSING,FOLDERNAME1,FILENAME1,YAMLFILE)

BEST_MODEL="best_model"
MODEL_PATH="model_path"


TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#variables for training pipeline config
TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"

#variables for dataingestion config
DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR="data ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY="raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY="tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_KEY="ingested_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY="ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY="ingested_test_dir"

#variables for datavalidation config
DATA_VALIDATION_CONFIG_KEY="data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR="data validation"
DATA_VALIDATION_SCHEMA_DIR_KEY="schema_dir"
DATA_VALIDATION_SCHEMA_FILENAME="schema_file_name"
DATA_VALIDATION_REPORT_FILENAME="report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILENAME="report_page_file_name"

#variables for datatransfoemation config
DATA_TRANSFORMATION_CONFIG_KEY="data_transformation_config"
DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM="add_bedroom_per_room"
DATA_TRANSFORMATION_TRANSFORMED_DIR="transformed_dir"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR="transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR="transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR="preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSING_OBJECT_FILENAME="preprocessed_object_file_name"
DATA_TRANSFORMATION_ARTIFACT_DIR="data transformation"

COLUMN_TOTAL_ROOMS = "total_rooms"
COLUMN_POPULATION = "population"
COLUMN_HOUSEHOLDS = "households"
COLUMN_TOTAL_BEDROOM = "total_bedrooms"
DATASET_SCHEMA_COLUMNS_KEY=  "columns"

NUMERICAL_COLUMN_KEY="numerical_columns"
CATEGORICAL_COLUMN_KEY = "categorical_columns"


TARGET_COLUMN_KEY="target_column"


# Model Training related variables

MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY = "model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY = "base_accuracy"
MODEL_TRAINER_MODEL_CONFIG_DIR_KEY = "model_config_dir"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY = "model_config_file_name"


MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"
MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"
