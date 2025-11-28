from fastapi import FastAPI
import pandas as pd

df = pd.read_csv("uno.csv", encoding="latin-1")
df.columns = df.columns.str.lower().str.strip()

app = FastAPI(title="iesazarquiel")

@app.get("/info-alumnos")
def info_alumnos():
    ids = df["id"].tolist()
    return {"ids_alumnos": ids}

@app.get("/asistencia")
def asistencia(id: int = None):
    if id is None:
        return {
            "error no has metido el id"
        }

    if id not in df["id"].values:
        return {"error ese alumno no existe"}

    alumno = df[df["id"] == id].iloc[0]
    return {
        "nombre": alumno["nombre"],
        "apellidos": alumno["apellidos"],
        "asistencia": alumno["asistencia"]
    }

@app.get("/notas")
def notas(id: int = None, nota: str = None):
    if id is None or nota is None:
        notas_disponibles = [col for col in df.columns if col not in ["id", "nombre", "apellidos", "asistencia"]]
        return {
            "error falta algun parametro"
            }
        

    if id not in df["id"].values:
        return {"error no existe el alumno ese alumno con ese id"}

    if nota not in df.columns:
        notas_disponibles = [col for col in df.columns if col not in ["id", "nombre", "apellidos", "asistencia"]]
        return {
            "erroren la nota no existe"
        }

    alumno = df[df["id"] == id].iloc[0]
    return {
        "nombre": alumno["nombre"],
        "apellidos": alumno["apellidos"],
        "nota": nota,
        "calificacion": alumno[nota]
    }