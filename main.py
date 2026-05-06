from app import app # importando o arquivo app 
from app.routers.itens import router #importar a rota
from app.routers.usuarios import router as usuarios_router # importando a rota de usuarios 
from app.database import Base, engine 


app.include_router(router) # registrar a rota dos itens
app.include_router(usuarios_router) # registrando a rota de usuarios 

Base.metadata.create_all(bind=engine)


if __name__ == "__main__": # se o arquivo esta sendo exutado diretamente 
    import uvicorn
#inciando Servidor      #sever local       #porta    
    uvicorn.run(app, host= "127.0.0.1", port=8000) 

