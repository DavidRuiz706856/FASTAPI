from fastapi import FastAPI
app = FastAPI()
@app.get("/miprimera-api") #ruta para acceder a la api

def saludo(name:str):
    return { f"Hola, {name}!"}