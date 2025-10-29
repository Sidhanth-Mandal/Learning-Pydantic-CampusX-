from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

#MODEL VALIDATOR IS USED WHEN TWO OR MORE FIELDS ARE INVOLVED AT A TIME TO VALIDATE 
#FOR EG : Patient more than 60 years of age must have an emergency contact passed in contact details 
#here validation is based on TWO fields age and contact_details 

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    #to achive this we use model_validator 

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model): # cls -> class instance , model -> all the values of that instance 
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)