from flask import Flask, render_template, request
import pandas as pd
import pickle

app=Flask(__name__)

model=pickle.load(open("seoul_data.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        hour=int(request.form["hour"])
        temperature=float(request.form["temperature"])
        humidity=float(request.form["humidity"])
        wind_speed=float(request.form["wind_speed"])
        visibility=float(request.form["visibility"])
        solar_radiation=float(request.form["solar_radiation"])
        rain_fall=float(request.form["rain_fall"])
        snow_fall=float(request.form["snow_fall"])
        seasons=request.form["seasons"]
        holidays=request.form["holidays"]
        functioning_day=request.form["functioning_day"]
        year=int(request.form["year"])
        month=int(request.form["month"])
        day=int(request.form["day"])
        weekday=int(request.form["week_day"])

        input_data=pd.DataFrame([{
            "Hour":hour,
            "Temperature(°C)":temperature,
            "Humidity(%)":humidity,
            "Wind speed (m/s)":wind_speed,
            "Visibility (10m)":visibility,
            "Solar Radiation (MJ/m2)":solar_radiation,
            "Rainfall(mm)": rain_fall,
            "Snowfall (cm)":snow_fall,
            "Seasons": seasons,
            "Holiday":holidays,
            "Functioning Day":functioning_day,
            "year":year,
            "month":month,
            "day":day,
            "weekday":weekday
        }])
        prediction=model.predict(input_data)[0]
        numerical_prediction=int(prediction)
        return render_template(
            "index.html",
            prediction_text=f"Estimated Bike demand: {numerical_prediction}"

        )
    except Exception as e:
        return str(e)
if __name__=="__main__":
    app.run(debug=True)

    