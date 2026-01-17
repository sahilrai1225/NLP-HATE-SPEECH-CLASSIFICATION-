import os

from datetime import datetime


## Common constants for this project
TIMESTAMP:str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") 
## when we will run everything will be at that timestamp
ARTIFACTS_DIR=os.path.join("artifacts",TIMESTAMP) ## ARTIFACTS DIR
BUCKET_NAME="hate_speech_nlp"
ZIP_FILE_NAME="dataset.zip"
LABEL="label"  ## dependent
TWEET="tweet"  ## independent



## DATA ingestion constants
DATA_INGESTION_ARTIFACTS_DIR="DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR="imbalace_data.csv"
DATA_INGESTION_RAW_DATA_DIR="raw_data.csv"