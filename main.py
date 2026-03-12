from fastapi import FastAPI , Path , HTTPException
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data


@app.get("/")
def home():
    return {"message": "Hello FastAPI 🚀"}

@app.get("/about")
def about():
    return {"message" : "Hey everyone i am ishan kumar tiwari"}

@app.get('/view')
def view_data():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description="id of the patient in DB", example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='patient not found')