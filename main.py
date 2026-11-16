from fastapi import FastAPI

app = FastAPI(
    title='Que paja pare', 
    description='Converjajion norma',
    version='v0.1'
)

@app.get('/')
def get_root(numero: str | None = None):
    return {'mensaje': numero}