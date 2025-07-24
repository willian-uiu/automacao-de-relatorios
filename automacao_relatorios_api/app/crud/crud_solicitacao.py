from sqlalchemy.orm import Session
from app.models.solicitacao import Solicitacao
from app.schemas.solicitacao import SolicitacaoCreate
from app.schemas.solicitacao import SolicitacaoUpdate
from datetime import *

def get_solicitacao_pendente(db: Session, *, revenda_id: str, setor_id: str) -> Solicitacao | None:
    """
    Busca uma solicitação com status 'pendente' para uma revenda e setor específicos.
    """
    return db.query(Solicitacao).filter(
        Solicitacao.revenda_id == revenda_id,
        Solicitacao.setor_id == setor_id,
        Solicitacao.status == "pendente"
    ).first()

def create_solicitacao(db: Session, *, solicitacao_in: SolicitacaoCreate) -> Solicitacao:
    """
    Cria uma nova solicitação no banco de dados.
    """
    # Agora passamos ambos os campos para o modelo
    db_obj = Solicitacao(
        revenda_id=solicitacao_in.revenda_id,
        setor_id=solicitacao_in.setor_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_proxima_solicitacao_pendente(db: Session) -> Solicitacao | None:
    """
    Busca a solicitação pendente mais antiga da fila (FIFO).
    """
    return db.query(Solicitacao).filter(Solicitacao.status == "pendente").order_by(Solicitacao.data_solicitacao.asc()).first()

def get_solicitacao(db: Session, *, id: int) -> Solicitacao | None:
    """
    Busca uma solicitação específica pelo seu ID.
    """
    return db.query(Solicitacao).filter(Solicitacao.id == id).first()

def update_solicitacao_status(db: Session, *, db_obj: Solicitacao, obj_in: SolicitacaoUpdate) -> Solicitacao:
    """
    Atualiza o status e a mensagem de log de uma solicitação.
    """
    db_obj.status = obj_in.status
    db_obj.log_mensagem = obj_in.log_mensagem

    # Atualiza os timestamps de processamento
    if obj_in.status == "processando":
        db_obj.data_inicio_proc = datetime.utcnow()
    elif obj_in.status in ["concluido", "erro"]:
        db_obj.data_fim_proc = datetime.utcnow()

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj