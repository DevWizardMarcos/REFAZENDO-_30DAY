from fastapi import APIRouter # fazendo a importação da rota de API
from app.schemas.itens import Item #importando o itens em Schemas

router = APIRouter() # Criando a rota de API




itens = [
    {'id': 1, 'nome':'Cafe'},
    {'id': 2, 'nome': 'Pao'}
]

# pegando a rota diretamente da API
@router.get("/itens") 

def listar_itens(nome = None): # Query Param
    if nome: #filtrando por nome (se passou por exemplo ?nome=Cafe na URL)
        for item in itens: 
            if item['nome'] == nome: 
                return item
    else:
        return itens #se nao passou nada

#criando a a rota POST 

@router.post('/itens')

                # mudando para respoeitar o modelo padrao
def criarItens(item:Item):
    novoId = len(itens) + 1 #criando novo id 
    novoItem =item.model_dump() # convertando o Pydantic em dicionario 
    novoItem['id'] = novoId # colocando um novo id 
    itens.append(novoItem) # adicionando na lista 
    return novoItem

#criando a rota para pegar o id 1 

@router.get("/itens/{id}") # usando PATH Param um valor que faz parte do caminho da URL 

def percorrer(id:  int): #parementro de tipo int que é o id
    for i in itens: 
        if i ['id'] == id: # se a chave i for == ao id 
            return i # retorna o chave e o valor 
        
