
from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome : str
    email: str
    username : str
    senha: str


class UsuarioResponse(BaseModel):
    id: int
    nome:str 
    email:str
    username:str 
    ativo: bool

    class Config:
        from_atributes : True 
    


    