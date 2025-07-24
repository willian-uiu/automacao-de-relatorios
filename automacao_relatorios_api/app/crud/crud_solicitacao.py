from sqlalchemy.orm import Session
from app.models.solicitacao import Solicitacao
from app.schemas.solicitacao import SolicitacaoCreate

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