from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Banco de dados fake de telemetria
vehicle_status = {
    "carro_1": {"lat": -23.55052, "lon": -46.633308, "speed": 40, "battery": 80},
    "carro_2": {"lat": -22.9068, "lon": -43.1729, "speed": 0, "battery": 100},
    "carro_3": {"lat": -23.55052, "lon": -46.633308, "speed": 50, "battery": 60},
}

# Modelo de resposta
class TelemetryResponse(BaseModel):
    vehicle_id: str
    lat: float
    lon: float
    speed: int
    battery: int

# Endpoint para obter telemetria do veículo
@app.get("/telemetry/{vehicle_id}", response_model=TelemetryResponse)
def get_telemetry(vehicle_id: str):
    data = vehicle_status.get(vehicle_id)
    if not data:
        return {"error": "Veículo não encontrado"}
    
    # Simular variação nos dados
    data["speed"] = max(0, data["speed"] + random.randint(-5, 5))
    data["battery"] = max(0, data["battery"] - random.randint(0, 2))

    return TelemetryResponse(vehicle_id=vehicle_id, **data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
