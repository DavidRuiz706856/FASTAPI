from fastapi import FastAPI
import pandas as pd

df = pd.read_csv("/practica1.3/datos_alumnos.csv")

app = FastAPI(title="iesazarquiel")

@app.get("/info-alumnos")
def info_alumnos():
    ids = df["id"].tolist()
    return {"ids_alumnos": ids}

@app.get("/asistencia")
def asistencia(id: int = None):
    if id is None:
        return {
            "mensaje": "este endpoint recibe 1 parámetro opcional llamado id",
            "uso": "/asistencia?id=ID_DEL_ALUMNO",
            "ejemplo": "/asistencia?id=3",
            "ids_disponibles": df["id"].tolist()
        }

    if id not in df["id"].values:
        return {
            "error": "id no encontrado",
            "ids_validos": df["id"].tolist()
        }

    alumno = df[df["id"] == id].iloc[0]
    return {
        "id": id,
        "nombre": alumno["nombre"],
        "apellidos": alumno["apellidos"],
        "asistencia_porcentaje": alumno["asistencia"]
    }

@app.get("/notas")
def notas(id: int = None, nota: str = None):
    if id is None and nota is None:
        return {
            "mensaje": "este endpoint recibe parámetros opcionales: id y nota",
            "parametro_id": "id del alumno",
            "parametro_nota": "nombre de la columna de nota",
            "notas_disponibles": [col for col in df.columns if col.startswith("nota")],
            "ejemplos": [
                "/notas?id=2&nota=nota_examen",
                "/notas?id=1&nota=nota_practicas"
            ]
        }

    if id is not None and id not in df["id"].values:
        return {
            "error": "id no encontrado",
            "ids_validos": df["id"].tolist()
        }

    if nota is not None and nota not in df.columns:
        return {
            "error": "nombre de nota incorrecto",
            "notas_validas": [col for col in df.columns if col.startswith("nota")]
        }

    alumno = df[df["id"] == id].iloc[0]
    return {
        "id": id,
        "nombre": alumno["nombre"],
        "apellidos": alumno["apellidos"],
        "nota_consultada": nota,
        "valor": alumno[nota]
    }