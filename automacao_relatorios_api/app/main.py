from fastapi import FastAPI
from app.api import endpoints

# Importe o Middleware de CORS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Automação de Relatórios")

# Lista de origens que podem fazer requisições à nossa API
# Para desenvolvimento, podemos permitir todas com "*"
origins = [
    "*", 
]

# Adiciona o middleware de CORS à aplicação
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, PUT, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)

# O resto do seu código continua igual
app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "API de Automação de Relatórios está no ar!"}