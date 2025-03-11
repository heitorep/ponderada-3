from fastapi import FastAPI
import requests

app = FastAPI()

# Rota de teste para verificar se o API Gateway está funcionando
@app.get("/")
def read_root():
    return {"message": "API Gateway funcionando!"}

# Proxy para autenticação
@app.post("/auth/login")
def login(user_data: dict):
    response = requests.post("http://localhost:8001/login", json=user_data)
    return response.json()

# Proxy para consulta de frota
@app.get("/fleet/availability")
def check_availability(location: str):
    response = requests.get(f"http://localhost:8002/availability?location={location}")
    return response.json()

# Proxy para pagamento
@app.post("/payment/process")
def process_payment(payment_data: dict):
    response = requests.post("http://localhost:8003/process", json=payment_data)
    return response.json()

# Proxy para telemetria
@app.get("/telemetry/{vehicle_id}")
def get_telemetry(vehicle_id: str):
    response = requests.get(f"http://localhost:8004/telemetry/{vehicle_id}")
    return response.json()

# Proxy para monitoramento e relatórios
@app.get("/monitoring/reports")
def get_reports():
    response = requests.get("http://localhost:8005/reports")
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
