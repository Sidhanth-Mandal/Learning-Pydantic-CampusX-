from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  #Gives a dict
temp = patient1.model_dump_json() # gives in json format ( python see it as a str )
temp = patient1.model_dump(include = ['name' , 'gender']) # Only gives 'name' , 'gender'
temp = patient1.model_dump(exclude = ['name' , 'gender']) # Gives everything expect 'name' , 'gender'

temp = patient1.model_dump(exclude_unset=True) #Only include the fields that the user actually provided when creating the model 
                                                    #— ignore any fields that just took their default values
print(temp)
print(type(temp))