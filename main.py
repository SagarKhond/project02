
from flask import Flask, jsonify, render_template, request
from model.utils import MedicalInsurance
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    return render_template("index.html")


@app.route('/predict_charges',methods=["POST","GET"])
def get_insurance_charges():
    if request.method=="GET":
        age = eval(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = eval(request.args.get("bmi"))
        children = eval(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)

    else:
        print("we are in post method")
        age = eval(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = eval(request.form.get("bmi"))
        children = eval(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")
        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)

    # data = request.form
    # print("Data ::",data)
    # age = eval(data['age'])
    # sex = data['sex']
    # bmi = eval(data['bmi'])
    # children = eval(data['children'])
    # smoker = data['smoker']
    # region = data['region']



    
        

        # age = eval(request.args.get("age"))
        # sex = request.args.get("sex")
        # bmi = eval(request.args.get("bmi"))
        # children = eval(request.args.get("children"))
        # smoker = request.args.get("smoker")
        # region = request.args.get("region")

    # print(age, sex, bmi, children, smoker, region)
    # med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    # charges = med_ins.get_predicted_price()
    # # return render_template("index.html",prediction=charges)
    # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})
        

      
        

    # else:
    #     print("we are in POST method")

    #     age = eval(request.form.get("age"))
    #     sex = request.form.get("sex")
    #     bmi = eval(request.form.get("bmi"))
    #     children = eval(request.form.get("children"))
    #     smoker = request.form.get("smoker")
    #     region = request.form.get("region")   

    #     print(age, sex, bmi, children, smoker, region)
    #     med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)
    #     #return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})

    


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=config.PORT_NUMBER, debug=True)