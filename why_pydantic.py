#------------------------------------ BASIC PYDANTIC --------------------------------------------

from pydantic import BaseModel
class Patient(BaseModel):
    
    #type check 
    name: str
    age: int


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print("INSERTED")

# even string '20' is automatically converted by pydantic into 20 int
patient_1 = {'name' : 'Sidhanth' , 'age' : '20'}


#insert_patient_data(Patient(**patient_1))


#--------------------------------- MORE COMPLEX PYDANTIC -----------------------------------------


from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    #Using combination of Field and Annotated we can assign tittle , description , examples etc to any parameter 
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    
    #EmaiStr is custom datatype pydantic give which can validate a email address
    email: EmailStr

    #AnyUrl is custom datatype pydantic give which can validate a URL 
    linkedin_url: AnyUrl

    #Using Field we could assign limits to parameters
    age: int = Field(gt=0, lt=120)

    #Using strict = True we can stop pydantic to automatically type conversion ( for example str '20' is converted to int 20 -> but this can be dangerous )
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

    #To validadate datatype inside a list or dict we have to use List , Dict from Typing module 
    #By using Optional[] -> not a necessary parameter to provide , note -> always define default value while using optional 
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


