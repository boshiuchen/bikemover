from flask import Flask, render_template, request
# from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
# moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/DataProcessing')
def DataProcessing():
    return render_template('DataProcessing.html')

@app.route('/ana-general')
def analysisGeneral():
    return render_template('ana-general.html')

@app.route('/ana-holiday')
def analysisHoliday():
    return render_template('ana-holiday.html')

@app.route('/ana-nearbys')
def analysisNearbys():
    return render_template('ana-nearbys.html')

@app.route('/ana-weather')
def analysisWeather():
    return render_template('ana-weather.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')








# Repository https://github.com/boshiuchen/Youbike

# practice end

if __name__ == "__main__":
    app.run(debug=True)
