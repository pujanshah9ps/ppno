import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    print("aaa")
    print(request.form.get("Phone"))
    number = request.form.get("Phone")
    ch_nmber = phonenumbers.parse(number, "CH")
    service_nmber = phonenumbers.parse(number, "RO")
    output = geocoder.description_for_number(ch_nmber, "en") + "-" + carrier.name_for_number(service_nmber, "en")
    #output = output + "-" + str(phonenumbers.parse(number, "RO"))
    print("end")
    print(output)	
    return render_template('index.html', prediction_text='Phone Number belongs to - {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)