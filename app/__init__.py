from fastapi import FastAPI # importando o Fast 


app = FastAPI() # definindo para as rotas 


# criando a rota  GET  usando um decorador
@app.get("/health")

def health_check():
    return {
        'status': 200, # codigo de deu bom 
        'message': 'API está dando bom' # mensagem caso de bom 
    } # retorna um JSON

