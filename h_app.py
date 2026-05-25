from flask import Flask, render_template, request, jsonify
import json
import sys

import hospital
sys.path.append(".")
from hospital import Patient, CovidPatient, ICUPatient, load_patient, save_patient

app = Flask(__name__)

@app.route("/")
def home():
    hospital = load_patient()

    patient_data = []
    serious = 0
    critical = 0
    mild = 0
    
    for p in hospital:
    
        severity = p.check_severity()
        if "SERIOUS" in severity.upper():
            serious += 1
        elif "CRITICAL" in severity.upper():
            critical += 1
        else:
            mild += 1

        patient_data.append({
            "name" : p.name,
            "age" : p.age,
            "type" : type(p).__name__,
            "symptoms" : p.get_symptoms(),
            "bloodg" : p.get_bloodg(),
            "severity" : severity
        })
        
    return render_template("index.html", 
                        patient_count=len(hospital),
                        patients=patient_data, 
                        critical=critical,
                        serious=serious,
                        mild=mild)


@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        age = int(data["age"])
        symptoms = data["symptoms"]
        bloodg = data["bloodg"]
        ptype = data["type"]
        if ptype == "CovidPatient":
            oxygen = int(data["oxygen"])
            vaccinated = data["vaccinated"] == "true"
            p = CovidPatient(name, age, symptoms, bloodg, oxygen, vaccinated)
        elif ptype == "ICUPatient":
            ventilator = data["ventilator"] == "true"
            p = ICUPatient(name, age, symptoms, bloodg, ventilator)
        else:
            p = Patient(name, age, symptoms, bloodg)

        hospital = load_patient()
        hospital.append(p)
        save_patient(hospital)

        return jsonify({
            "success" : True,
            "message" : f"Patient {name} added succesfully"
        })       

    return render_template("add_patient.html")

if __name__ == "__main__":
    app.run(debug=True)
