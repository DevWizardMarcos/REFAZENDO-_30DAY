from app import app # importando o arquivo app 
from app.routers.itens import router #importar a rota

app.include_router(router) # registrar a rota dos itens

if __name__ == "__main__": # se o arquivo esta sendo exutado diretamente 
    import uvicorn
#inciando Servidor      #sever local       #porta    
    uvicorn.run(app, host= "127.0.0.1", port=8000) 

