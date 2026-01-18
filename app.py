from hate.pipeline.train_pipeline import TrainPipeline
from fastapi import FastAPI
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.exception import CustomException
from hate.constants import *


text:str ="what is machine learning"

app=FastAPI()
@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        train_pipeline=TrainPipeline()

        train_pipeline.run_pipeline()
        return Response("Training Successful")
    
    except Exception as e:
        return Response(f"Error occured {e}")
    

@app.post("/predict")
async def predict_route(text):

    try:

        obj=PredictionPipeline()
        text=obj.run_pipeline(text)

        return text
    
    except Exception as e:
        raise CustomException(e,sys) from e
    

if __name__=="__main__":
    uvicorn.run(app,host=APP_HOST,port=APP_PORT)
    

# from flask import Flask, render_template, request
# import sys
# from hate.pipeline.train_pipeline import TrainPipeline
# from hate.pipeline.prediction_pipeline import PredictionPipeline
# from hate.exception import CustomException
# from hate.constants import APP_HOST, APP_PORT

# app = Flask(__name__)

# # Home Page
# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")


# # Train Route
# @app.route("/train", methods=["GET"])
# def train():
#     try:
#         train_pipeline = TrainPipeline()
#         train_pipeline.run_pipeline()
#         return "✅ Training Successful"
#     except Exception as e:
#         return f"❌ Error Occurred: {e}"


# # Predict Route
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         text = request.form.get("text")

#         pipeline = PredictionPipeline()
#         result = pipeline.run_pipeline(text)

#         label = "HATE SPEECH " if result == 1 else "NOT HATE SPEECH "

#         return render_template(
#             "result.html",
#             text=text,
#             prediction=label
#         )

#     except Exception as e:
#         raise CustomException(e, sys) from e


# if __name__ == "__main__":
#     app.run(host=APP_HOST, port=APP_PORT, debug=True)
