from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    #To make custom validator we use @field_validator method ( decorators )

    @field_validator('email')
    @classmethod

    def email_validator(cls, value):  # cls -> class instance , value -> value of the attached parameter ( here 'email')
        
        """When you define a class method (using @classmethod), 
        the first argument is cls, which refers to the class itself, not an individual instance."""

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    

    #Can be used to transform the value
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    


    @field_validator('age', mode='after')
    #By default the mode is 'after' , this refers to as when to apply validator thatis 
    #Before type coercion or after 
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)