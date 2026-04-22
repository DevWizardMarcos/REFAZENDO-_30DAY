from fastapi import FastAPI # importando o Fast 
from pydantic import BaseModel # definir o modelo padrao

app = FastAPI() # definindo para as rotas 


class Item(BaseModel):
    nome: str



# criando a rota  GET  usando um decorador
@app.get("/health")

def health_check():
    return {
        'status': 200, # codigo de deu bom 
        'message': 'API está dando bom' # mensagem caso de bom 
    } # retorna um JSON

 
itens = [
    {'id': 1, 'nome':'Cafe'},
    {'id': 2, 'nome': 'Pao'}
]

# criado a rota de itens
@app.get("/itens")

def listar_itens(nome = None): # Query Param
    if nome: #filtrando por nome (se passou por exemplo ?nome=Cafe na URL)
        for item in itens: 
            if item['nome'] == nome: 
                return item
    else:
        return itens #se nao passou nada

#criando a a rota POST 

@app.post('/itens')

                # mudando para respoeitar o modelo padrao
def criarItens(item:Item):
    novoId = len(itens) + 1 #criando novo id 
    item['id'] = novoId # colocando um novo id 
    itens.append(item) # adicionando na lista 
    return item

#criando a rota para pegar o id 1 

@app.get("/itens/{id}") # usando PATH Param um valor que faz parte do caminho da URL 

def percorrer(id:  int): #parementro de tipo int que é o id
    for i in itens: 
        if i ['id'] == id: # se a chave i for == ao id 
            return i # retorna o chave e o valor 
        
