from flask import Flask, render_template, jsonify, request
import config
from Project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route('/')   # Home API

def base():
    print('Hello, How are you?')
    return render_template('home.html')

####################################################################

@app.route('/predicted_charges')
def get_insurance_charges():
    age = 35
    sex = 'male'
    bmi = 27.9
    children = 3
    smoker = 'yes'
    region = 'northeast'

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()

    return jsonify ({'Result': f'Predicted Medical insurance is: {charges}'})


if __name__ == '__main__':
    app.run()