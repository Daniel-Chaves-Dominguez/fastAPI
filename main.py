from fastapi import FastAPI

from routes import perros

app = FastAPI(
    title='Que paja pare',
    description='Converjajion norma',
    version='v0.1'
)

app.include_router(perros.router)


@app.get('/')
def get_root(numero: str | None = None):
    return {'mensaje': numero}
