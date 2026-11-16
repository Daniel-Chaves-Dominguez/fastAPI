from pydantic import BaseModel, Field

class Perro(BaseModel):
    nombre: str = Field(min_length=2, max_length=20)
    chip: bool = False
    raza: str | None = None
    edad: int = Field(ge=0, description='La edad del perrito')
    vacunas: list[str] = []
