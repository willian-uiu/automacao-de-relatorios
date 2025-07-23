from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema para os dados que recebemos ao criar uma solicitação
class SolicitacaoCreate(BaseModel):
    revenda_id: str
    setor_id: str

# Schema para os dados que recebemos ao atualizar o status
class SolicitacaoUpdate(BaseModel):
    status: str
    log_mensagem: Optional[str] = None

# Schema base para os dados que enviamos de volta na resposta da API
class Solicitacao(BaseModel):
    id: int
    revenda_id: str
    setor_id: str
    status: str
    data_solicitacao: datetime
    data_inicio_proc: Optional[datetime] = None
    data_fim_proc: Optional[datetime] = None
    log_mensagem: Optional[str] = None

    # Configuração para dizer ao Pydantic que ele pode ler dados de um objeto ORM
    class Config:
        orm_mode = True