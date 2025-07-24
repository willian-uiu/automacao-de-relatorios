from fastapi import FastAPI
from app.api import endpoints

# Cria a instância principal da aplicação FastAPI
app = FastAPI(title="API de Automação de Relatórios")

# Inclui o roteador com nosso endpoint
app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "API de Automação de Relatórios está no ar!"}