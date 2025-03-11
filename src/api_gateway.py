from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Configuração dos endpoints dos microserviços
SERVICES = {
    "auth": "http://localhost:8001",
    "fleet": "http://localhost:8002",
    "payment": "http://localhost:8003",
    "telemetry": "http://localhost:8004",
    "monitoring": "http://localhost:8005",
}

async def forward_request(service: str, method: str, endpoint: str, payload=None):
    """Encaminha a requisição para o microserviço correto."""
    url = f"{SERVICES[service]}{endpoint}"
    
    async with httpx.AsyncClient() as client:
        if method == "GET":
            response = await client.get(url)
        elif method == "POST":
            response = await client.post(url, json=payload)
        elif method == "PUT":
            response = await client.put(url, json=payload)
        elif method == "DELETE":
            response = await client.delete(url)
        else:
            raise HTTPException(status_code=400, detail="Método HTTP inválido")
    
    return response.json()

# Rotas do API Gateway
@app.get("/auth/{path:path}")
async def proxy_auth(path: str):
    return await forward_request("auth", "GET", f"/{path}")

@app.post("/auth/{path:path}")
async def proxy_auth_post(path: str, payload: dict):
    return await forward_request("auth", "POST", f"/{path}", payload)

@app.get("/fleet/{path:path}")
async def proxy_fleet(path: str):
    return await forward_request("fleet", "GET", f"/{path}")

@app.post("/fleet/{path:path}")
async def proxy_fleet_post(path: str, payload: dict):
    return await forward_request("fleet", "POST", f"/{path}", payload)

@app.get("/payment/{path:path}")
async def proxy_payment(path: str):
    return await forward_request("payment", "GET", f"/{path}")

@app.post("/payment/{path:path}")
async def proxy_payment_post(path: str, payload: dict):
    return await forward_request("payment", "POST", f"/{path}", payload)

@app.get("/telemetry/{path:path}")
async def proxy_telemetry(path: str):
    return await forward_request("telemetry", "GET", f"/{path}")

@app.get("/monitoring/{path:path}")
async def proxy_monitoring(path: str):
    return await forward_request("monitoring", "GET", f"/{path}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
