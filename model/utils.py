
import pickle
import json
import numpy as np
import config

class MedicalInsurance():
  def __init__(self,age, sex, bmi, children, smoker, region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_" + region

  def load_model(self):

      with open(config.MODEL_FILE_PATH,"rb") as f:
          self.model=pickle.load(f)    
      with open(config.JSON_FILE_PATH,"r") as f:
          self.json_data=json.load(f)

  def get_predicted_price(self):
        self.load_model()

        region_index=self.json_data["column"].index(self.region)

        array=np.zeros(len(self.json_data["column"]))
        array[0]=self.age
        array[1]=self.json_data["sex"][self.sex]
        array[2]=self.bmi
        array[3]=self.children
        array[4]=self.json_data["smoker"][self.smoker]
        array[region_index]=1

        print("Test array-->>/n",array)
        predicted_charges=self.model.predict([array])[0]

        return np.around(predicted_charges,2)        
    


if __name__ == "__main__":
    age=30
    sex="male"
    bmi=40
    children=1
    smoker="yes"
    region="northwest"
    
    med_ins=MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges=med_ins.get_predicted_price()
    print()
    print(f"The predicted charges for Medical insurance is {charges} -\Rs. only")