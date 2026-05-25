import json

class Patient:
    def __init__(self, name, age, symptoms, bloodg):
        self.name = name
        self.__symptoms = symptoms
        self.__bloodg = None
        self.update_bloodg(bloodg)

        if age < 0 or age > 120:
            print(f"Warning: Invalid age {age} for {name}. Setting to 0.")
            self.age = 0
        else:
            self.age = age


    def get_report(self):
        print("Status: Under observation")
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Symptoms: {self.__symptoms}")
        print(f"Blood Group: {self.__bloodg}")
        print("Severity     :", self.check_severity())
        print("----------------------------")

    def check_severity(self):
        serious = ["fever", "headache", "stomach pain", "unconscious"]

        for words in serious:
            if words in self.__symptoms.lower():
                return "SERIOUS — needs immediate attention"
        return "MILD — can be treated with home care"
    
    def get_symptoms(self):
        return self.__symptoms
    
    def update_symptoms(self, new_symptoms):
        if len(new_symptoms) < 3:
            print("Symptoms cannot be updated. Severity is too low.")
        else:
            self.__symptoms = new_symptoms
            print("Symptoms updated successfully.")
    def get_bloodg(self):
        return self.__bloodg
    
    def update_bloodg(self, new_bg):
        valid = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        if new_bg in valid:
            self.__bloodg = new_bg
        else:
            print(f"Invalid blood group: {new_bg}. Blood group not updated.")
    
    def to_dict(self):
        return {
        "type" : "Patient",
        "name" : self.name,
        "age" : self.age,
        "symptoms" : self.__symptoms,
        "bloodg" : self.__bloodg
    }


class CovidPatient(Patient):
    def __init__(self, name, age, symptoms, bloodg, oxygen, vaccinated):
        super().__init__(name, age, symptoms, bloodg)
        self.oxygen = oxygen
        self.vaccinated = vaccinated

    def get_report(self):
        super().get_report()
        print(f"Oxygen Level: {self.oxygen}%")
        print(f"Vaccination Status: {'Vaccinated' if self.vaccinated else 'Not Vaccinated'}")
        print("----------------------------")
    def check_severity(self):
        if self.oxygen < 95:
            return "Critical — oxygen level dangerously low"
        return super().check_severity()
    
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "CovidPatient"
        data["oxygen"] = self.oxygen
        data["vaccinated"] = self.vaccinated
        return data

class ICUPatient(Patient):
    def __init__(self, name, age, symptoms, bloodg, ventilator):
        super().__init__(name, age, symptoms, bloodg)
        self.ventilator = ventilator
    
    def get_report(self):
        super().get_report()
        print(f"Ventilator Required: {'Yes' if self.ventilator else 'No'}")
        print("----------------------------")

    def check_severity(self):
        if self.ventilator:
            return "Critical — requires ventilator support"
        return super().check_severity()
    
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "ICUPatient"
        data["ventilator"] = self.ventilator
        return data
    
def save_patient(patient_list):
    data = [p.to_dict() for p in patient_list]
    with open("patient.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f'Saved {len(patient_list)} patients to file.')

def load_patient():
    try:
        with open("patient.json", "r") as f:
            data = json.load(f)

        patient = []
        for items in data:
            if items["type"] == "CovidPatient":
                p = CovidPatient(items["name"], items["age"], items["symptoms"], items["bloodg"], items["oxygen"], items["vaccinated"])
            elif items["type"] == "ICUPatient":
                p = ICUPatient(items["name"], items["age"], items["symptoms"], items["bloodg"], items["ventilator"])
            else:
                p = Patient(items["name"], items["age"], items["symptoms"], items["bloodg"])
            patient.append(p)

        print(f"Loaded {len(patient)} from file.")
        return patient
    
    except FileNotFoundError:
        print("No patient data file found. Starting with an empty list.")
        return []
    
if __name__ == "__main__":
    hospital = []
    hospital.append(Patient("Ravi", 45, "fever", "O+"))
    hospital.append(CovidPatient("Deepak", 55, "fever and breathing", "B+", 94, True))
    hospital.append(ICUPatient("Ramesh", 67, "unconscious", "O-", True))

    save_patient(hospital)

    hospital = []
    print("List cleared. Patients in memory:", len(hospital))

    hospital = load_patient()
    print("Patients after loading:", len(hospital))

    for p in hospital:
        p.get_report()