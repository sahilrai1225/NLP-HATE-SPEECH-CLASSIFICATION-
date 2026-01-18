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
DATA_INGESTION_IMBALANCE_DATA_DIR="imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR="raw_data.csv"


## DATA transformation constants
DATA_TRANSAFORMATION_ARTIFACTS_DIR="DataTransformationArtifacts"
TRANSFORMED_FILE_NAME="final.csv"
DATA_DIR="data"
ID="id"
AXIS=1
INPLACE=True
DROP_COLUMNS=["Unnamed: 0","count","hate_speech","offensive_language","neither"]
CLASS="class"