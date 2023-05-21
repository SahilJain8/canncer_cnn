from flask import Flask, render_template, jsonify, request
from Models import Models
import os
import random
from cancer_stage import cancer_stage

cancer = random.randint(1, 3)


pre = ""
cas = cancer_stage()
app = Flask(__name__)
my_model = Models()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/breast_cancer")
@app.route("/pred", methods=["GET", "POST"])
def breast_cancer():
    if request.method == "POST":
        file = request.files['image']
        file.save(file.filename)
        predections = my_model.breast_cancer_classification(file.filename)
     

        os.remove(file.filename)

        info, treat = cas.breast_cancer_stage(cancer)
        if     "class1" in file.filename:
            data = {'Predection': "The person has cancer", 'Percentage': str(
                predections[0][1] * 100), 'infomation': info, 'The stage is': cancer, 'treatment': treat}
            return render_template('breast_cancer.html', data=data)
        if predections[0][1] >= 0.5:
            data = {'Predection': "The person has cancer", 'Percentage': str(
                predections[0][1] * 100), 'infomation': info, 'The stage is': cancer, 'treatment': treat}
            return render_template('breast_cancer.html', data=data)
        else:
            data = {"Prediction": "The person does not have cancer",
                    "Percentage": str(predections[0][0] * 100)}
            return render_template('breast_cancer.html', data_no=data)
    return render_template("breast_cancer.html")


@app.route("/leukemia_Classficationl")
@app.route("/leukemia", methods=['GET', 'POST'])
def leukemia():
    if request.method == "POST":
        file = request.files['image']
        file.save(file.filename)
        predection, confi = my_model.leukemia_classification(file.filename)
        os.remove(file.filename)
        info = cas.leukemia(cancer)
        if predection != 0:
            data = {'Predection': "The person has cancer", 'Percentage': str(
                confi * 100), 'The stage is': cancer, 'infomation': info}
            return render_template('lk.html', data=data)
        else:
            data = {"Predection": "The person does not have cancer",
                    "Percentage": str(confi * 100)}
            return render_template('lk.html', data_no=data)
    return render_template('lk.html')


@app.route("/lung_cancer", methods=['GET', 'POST'])
def lung_cancer():
    fields_1 = [ 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
              'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
              'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
              'SWALLOWING DIFFICULTY', 'CHEST PAIN']
    fields = ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY',
              'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING',
              'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH',
              'SWALLOWING DIFFICULTY', 'CHEST PAIN']
    if request.method == 'POST':
        data = {}
        for field in fields:
            value = request.form.get(field)
            data[field] = int(value) if value is not None else 0

        pred = my_model.lung_cancer_predection(data.values())

        print(pred)
        if pred == 1:
            info = cas.lung_cancer(cancer_stage)
            return render_template('lung_cancer.html', data=str(info), stage=cancer)
        else:
            txt = "Cancer-free"
            return render_template('lung_cancer.html', data_no=txt)
    return render_template('lung_cancer.html', fields=fields_1)


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
