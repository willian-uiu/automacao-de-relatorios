from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func

# Importa a Base que acabamos de criar
from app.db.base import Base

class Solicitacao(Base):
    __tablename__ = "solicitacoes"

    id = Column(Integer, primary_key=True, index=True)
    revenda_id = Column(String(50), nullable=False, index=True)
    setor_id = Column(String(50), nullable=False, index=True)
    status = Column(String(20), nullable=False, default="pendente")
    data_solicitacao = Column(DateTime(timezone=True), server_default=func.now())
    data_inicio_proc = Column(DateTime(timezone=True), nullable=True)
    data_fim_proc = Column(DateTime(timezone=True), nullable=True)
    log_mensagem = Column(Text, nullable=True)