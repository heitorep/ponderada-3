from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Simulação de frota disponível
fake_fleet_db = [
    {"id": "carro_1", "type": "autônomo", "location": "São Paulo", "available": True},
    {"id": "carro_2", "type": "autônomo", "location": "Rio de Janeiro", "available": False},
    {"id": "carro_3", "type": "humano", "location": "São Paulo", "available": True},
]

# Modelo de resposta
class Vehicle(BaseModel):
    id: str
    type: str
    location: str
    available: bool

# Endpoint para consultar veículos disponíveis por localização
@app.get("/availability", response_model=List[Vehicle])
def check_availability(location: str):
    available_vehicles = [v for v in fake_fleet_db if v["location"] == location and v["available"]]
    return available_vehicles

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
