from flask import Flask, request, jsonify,render_template
import testing
import Diabetes_db

app = Flask(__name__)


@app.route('/get_predict_diabeties', methods=['GET','POST'])
def get_predict_diabeties():
    if request.method == 'POST':
        data = request.form
        Preg = int(request.form['Pregnancies'])
        gluco = int(request.form['Glucose'])
        BP = int(request.form['BloodPressure'])
        ST = int(request.form['SkinThickness'])
        Ins = int(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        diabetiespred = float(request.form['DiabetesPedigreeFunction'])
        age = int(request.form['Age'])
        print('Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age',Preg,gluco,BP,ST,Ins,bmi,diabetiespred,age)
        predi = testing.decision_tree().predict_diab(3,61,82,28,0,34.4,0.243,46)
        Diabetes_db.save_diabetes_details(Preg,gluco,BP,ST,Ins,bmi,diabetiespred,age)
                
        return "The Predicted diabeties is {} ".format(predi)

    
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=False)