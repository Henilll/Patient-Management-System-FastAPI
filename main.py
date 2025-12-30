from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
from fastapi.middleware.cors import CORSMiddleware
import json

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
    return data

def save_data(data):
    with open("patients.json",'w') as f:
        json.dump(data,f)

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Id of the Patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="Name of the Patient",examples=["Rahul Sharma"])]
    city:Annotated[str,Field(...,description="City Where The Patient is living",examples=["Ahmedabad"])]
    age:Annotated[int,Field(...,description="Age Of The Patient",examples=[29],gt=0,lt=120)]
    gender:Annotated[Literal['Male','Female','Other'],Field(...,description="Gender Of the Patients")]
    height:Annotated[float,Field(...,gt=0,description="Height Of The Patient")]
    weight:Annotated[float,Field(...,description="Weight Of the Patinet")]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi<30:
            return 'Overweight'
        else:
            return 'Obese'

@app.get("/")
def home():
    return {"message":"Patient Management System API"}

@app.get("/about")
def about():
    return{"message":"Fully Functional API To Manage Your Patients Records"}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/view/{patient_id}")
def view_patient(patient_id:str=Path(...,description="ID Of The Patient In Db",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(404,detail="Patient Not Found")

@app.get("/sort")
def sort(sort_by: str = Query(...), ordered: str = Query('asc')):
    sort_fields = ['height', 'weight', 'bmi']
    sort_type = ['asc', 'desc']

    if sort_by not in sort_fields:
        raise HTTPException(400, detail=f"Cannot sort by {sort_by}")
    if ordered not in sort_type:
        raise HTTPException(400, detail=f"Invalid order {ordered}")

    data = load_data()
    patients = []

    for pid, pdata in data.items():
        p = Patient(id=pid, **pdata)
        patients.append(p.model_dump())

    reverse = ordered == "desc"

    return sorted(
        patients,
        key=lambda x: x[sort_by],
        reverse=reverse
    )

@app.post("/create")
def create_patient(patient:Patient):
    data=load_data()

    if patient.id in data:
        raise HTTPException(400,detail="Patient Already Exits")
    
    data[patient.id]=patient.model_dump(exclude=['id'])
    save_data(data)
    JSONResponse(content="New Patient Record Inserted",status_code=201)
    return {"message": "New Patient Record Inserted"}


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
    gender: Annotated[Optional[Literal['male', 'female', 'other']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


@app.patch("/edit/{patient_id}")
def update(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found")

    existing_patient = data[patient_id]

    updated_fields = patient_update.model_dump(exclude_unset=True)
    existing_patient.update(updated_fields)

    # validate full object
    patient_obj = Patient(id=patient_id, **existing_patient)

    # save validated data (without id)
    data[patient_id] = patient_obj.model_dump(exclude=['id'])

    save_data(data)

    return {"message": "Patient Details Updated Successfully"}

@app.delete('/delete/{patient_id}')
def remove_patient(patient_id:str):
    data=load_data()

    if patient_id not in data:
        raise HTTPException(400,detail="Patient Not Found..!")
    
    del data[patient_id]
    save_data(data)

    return {"message":"Patient Removed...!"}
