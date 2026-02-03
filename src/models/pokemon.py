from sqlmodel import Field, SQLModel
from pydantic import BaseModel

# entity
class Pokemon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=50)
    nivel: int = Field(ge=1, le=100)
    ataque: int = Field(ge=0)
    defensa: int = Field(ge=0)

# dto classes
class PokemonCreate(BaseModel):
    nombre: str
    nivel: int
    ataque: int
    defensa: int

class PokemonUpdate(BaseModel):
    nombre: str | None = None
    nivel: int | None = None
    ataque: int | None = None
    defensa: int | None = None

class PokemonResponse(BaseModel):
    id: int
    nombre: str
    nivel: int
    ataque: int
    defensa: int

# mapping functions
def map_pokemon_to_response(pokemon: Pokemon) -> PokemonResponse:
    return PokemonResponse(
        id=pokemon.id,
        nombre=pokemon.nombre,
        nivel=pokemon.nivel,
        ataque=pokemon.ataque,
        defensa=pokemon.defensa
    )

def map_create_to_pokemon(pokemon_create: PokemonCreate) -> Pokemon:
    return Pokemon(
        nombre=pokemon_create.nombre,
        nivel=pokemon_create.nivel,
        ataque=pokemon_create.ataque,
        defensa=pokemon_create.defensa
    )

def map_update_to_pokemon(pokemon: Pokemon, pokemon_update: PokemonUpdate) -> Pokemon:
    if pokemon_update.nombre is not None:
        pokemon.nombre = pokemon_update.nombre
    if pokemon_update.nivel is not None:
        pokemon.nivel = pokemon_update.nivel
    if pokemon_update.ataque is not None:
        pokemon.ataque = pokemon_update.ataque
    if pokemon_update.defensa is not None:
        pokemon.defensa = pokemon_update.defensa
    return pokemon
