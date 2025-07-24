from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db.session import SessionLocal

router = APIRouter()

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/solicitacoes", response_model=schemas.Solicitacao, status_code=201)
def create_solicitacao(
    *,
    db: Session = Depends(get_db),
    solicitacao_in: schemas.SolicitacaoCreate
):
    """
    Cria uma nova solicitação de relatório.
    """
    # A verificação agora usa ambos os IDs
    solicitacao_existente = crud.get_solicitacao_pendente(
        db=db,
        revenda_id=solicitacao_in.revenda_id,
        setor_id=solicitacao_in.setor_id
    )
    if solicitacao_existente:
        raise HTTPException(
            status_code=409, # Conflict
            detail="Já existe uma solicitação pendente para esta revenda e setor.",
        )
    
    solicitacao = crud.create_solicitacao(db=db, solicitacao_in=solicitacao_in)
    return solicitacao