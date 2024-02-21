from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from housing.logger import logging
from housing.exception import HousingException
import sys 
from housing.pipeline.predict_pipeline import HousingData
from housing.pipeline.predict_pipeline import Predictpipeline

application=Flask(__name__)
app=application

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        longitude = float(request.form['longitude'])
        latitude = float(request.form['latitude'])
        housing_median_age = float(request.form['housing_median_age'])
        total_rooms = float(request.form['total_rooms'])
        total_bedrooms = float(request.form['total_bedrooms'])
        population = float(request.form['population'])
        households = float(request.form['households'])
        median_income = float(request.form['median_income'])
        ocean_proximity = request.form['ocean_proximity']

        housing_data = HousingData(longitude=longitude,
                                   latitude=latitude,
                                   housing_median_age=housing_median_age,
                                   total_rooms=total_rooms,
                                   total_bedrooms=total_bedrooms,
                                   population=population,
                                   households=households,
                                   median_income=median_income,
                                   ocean_proximity=ocean_proximity,
                                   )
        housing_df = housing_data.get_housing_input_data_frame()
        print(housing_df)
        print("Before Prediction")

        predict_pipeline=Predictpipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(housing_df)
        print("after Prediction")
        return render_template('home.html',results=round(results[0],2))
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        
