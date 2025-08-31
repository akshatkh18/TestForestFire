from flask import Flask, request, jsonify, render_template
import pandas as pd 
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler 

application = Flask(__name__)
app=application 

## Import ridge regreesorand standardscaler pickle file 
ridge_model=pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler=pickle.load(open('models/scaler.pkl', 'rb'))

 

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=="POST":
        temp = float(request.form['Temperature'])
        rh = float(request.form['RH'])
        ws = float(request.form['Ws'])
        rain = float(request.form['Rain'])
        ffmc = float(request.form['FFMC'])
        dmc = float(request.form['DMC'])
        # dc = float(request.form['DC'])
        isi = float(request.form['ISI'])
        classes = float(request.form['Classes'])
        region = float(request.form['Region'])

        new_data_scaled=standard_scaler.transform( [[temp, rh, ws, rain, ffmc, dmc, isi, classes, region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html', results=result[0])


    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")


