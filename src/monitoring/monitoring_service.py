from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import datetime
import random

app = FastAPI()

# Banco de dados fake de histórico de viagens
travel_history = [
    {"vehicle_id": "carro_1", "distance_km": 15, "duration_min": 25, "timestamp": "2025-03-11T10:00:00"},
    {"vehicle_id": "carro_2", "distance_km": 10, "duration_min": 20, "timestamp": "2025-03-11T09:30:00"},
    {"vehicle_id": "carro_3", "distance_km": 30, "duration_min": 40, "timestamp": "2025-03-11T08:45:00"},
]

# Modelo de resposta para relatórios
class TravelReport(BaseModel):
    vehicle_id: str
    total_distance_km: float
    total_duration_min: int
    avg_speed: float

# Função para gerar um relatório por veículo
def generate_report(vehicle_id: str):
    trips = [t for t in travel_history if t["vehicle_id"] == vehicle_id]
    if not trips:
        return None
    
    total_distance = sum(t["distance_km"] for t in trips)
    total_duration = sum(t["duration_min"] for t in trips)
    avg_speed = total_distance / (total_duration / 60) if total_duration > 0 else 0

    return TravelReport(
        vehicle_id=vehicle_id,
        total_distance_km=total_distance,
        total_duration_min=total_duration,
        avg_speed=round(avg_speed, 2),
    )

# Endpoint para consultar estatísticas de um veículo
@app.get("/report/{vehicle_id}", response_model=TravelReport)
def get_report(vehicle_id: str):
    report = generate_report(vehicle_id)
    if not report:
        return {"error": "Nenhum dado encontrado para este veículo"}
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
