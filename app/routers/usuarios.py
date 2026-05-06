from fastapai import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from app.database import get_db, User 
from app.shemas.usuarios import UsuarioCreate, UsuarioResponse 

router = APIRouter()

@router.post('/usuarios',response_model =UsuarioResponse, status_code = 201)
def criar_usuario(usuario:UsuarioCreate, db:Session = Depends(get_db)):
    #vericando se o email ou usuario existe 
    if db.query(User).filter(User.email == usuario.email).first():
        raise HTTPException(status_code = 400, details = 'Email já cadastrado')
    if db.query(User).filter(User.username == usuario.username).first():
        raise HTTPException(status_code = 400, detail = 'Usuario ja cadastrado')
    
    novo = User(
        nome = usuario.nome, 
        email = usuario.email,
        username = usuario.username,
        senha = usuario.senha, # sem hash por hora
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
