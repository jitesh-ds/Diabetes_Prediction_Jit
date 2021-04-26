from pymongo import MongoClient

myclient = MongoClient('mongodb://localhost:27017/')
db = myclient['Diabetes_database']
Diabetes_user = db['user_details']
Diabetes_prediction = db['prediction_details']




def save_diabetes_details(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    diabetes_patient_details = {"Pregnancies": Pregnancies, "Glucose":Glucose,"BloodPressure":BloodPressure,
    "SkinThickness": SkinThickness,"Insulin":Insulin,"BMI":BMI,'DiabetesPedigreeFunction':DiabetesPedigreeFunction,"Age":Age}

    Diabetes_prediction.insert(diabetes_patient_details)

    return "Saved Successfully"