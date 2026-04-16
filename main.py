from app import app # importando o arquivo app 


if __name__ == "__main__": # se o arquivo esta sendo exutado diretamente 
    import uvicorn
#inciando Servidor      #sever local       #porta    
    uvicorn.run(app, host= "127.0.0.1", port=8000) 

