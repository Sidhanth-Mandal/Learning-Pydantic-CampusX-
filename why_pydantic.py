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


insert_patient_data(Patient(**patient_1))


