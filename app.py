from fastapi import FastAPI # importando o Fast 

app = FastAPI() # definindo para as rotas 


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

def listar_itens():
    return itens

#criando a a rota POST 

@app.post('/itens')

def criarItens(item:dict):
    novoId = len(itens) + 1 #criando novo id 
    item['id'] = novoId # colocando um novo id 
    itens.append(item) # adicionando na lista 
    return item
