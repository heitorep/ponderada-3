from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Banco de dados fake para simulação
fake_users_db = {
    "user@example.com": {
        "password": "123456",
        "name": "Usuário Teste",
        "role": "motorista"
    }
}

# Modelo de requisição para login
class LoginRequest(BaseModel):
    email: str
    password: str

# Rota de login
@app.post("/login")
def login(request: LoginRequest):
    user = fake_users_db.get(request.email)
    
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {"message": "Login bem-sucedido", "user": {"name": user["name"], "role": user["role"]}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
