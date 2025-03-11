from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Modelo de requisição para pagamento
class PaymentRequest(BaseModel):
    user_id: str
    vehicle_id: str
    amount: float
    payment_method: str  # "credit_card", "pix", "boleto"

# Modelo de resposta
class PaymentResponse(BaseModel):
    transaction_id: str
    status: str
    message: str

# Simulação de processamento de pagamento
@app.post("/process", response_model=PaymentResponse)
def process_payment(request: PaymentRequest):
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor do pagamento inválido")
    
    # Simulação de aprovação (80% de chance de sucesso)
    success = random.random() < 0.8
    status = "aprovado" if success else "recusado"
    message = "Pagamento aprovado!" if success else "Falha no pagamento, tente novamente."

    return PaymentResponse(
        transaction_id=f"TXN-{random.randint(1000, 9999)}",
        status=status,
        message=message
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
