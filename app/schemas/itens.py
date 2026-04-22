from pydantic import BaseModel # definir o modelo padrao


class Item(BaseModel): #criando o schama
    nome: str
    preco : float