from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from sqlmodel import Session
from models.pokemon import Pokemon, PokemonCreate, PokemonResponse, map_pokemon_to_response, map_create_to_pokemon

from data.pokemons_repository import PokemonsRepository
from data.db import init_db, get_session

router = APIRouter(prefix="/api/pokemons", tags=["pokemons"])

SessionDep = Annotated[Session, Depends(get_session)]

# Rutas de la API para gestionar series

@router.get("/", response_model=list[PokemonResponse])
async def lista_pokemons(session: SessionDep):
    repo = PokemonsRepository(session)
    pokemons = repo.get_all_pokemons()
    return [map_pokemon_to_response(pokemon) for pokemon in pokemons]

@router.post("/", response_model=PokemonResponse)
async def nuevo_pokemon(pokemon_create: PokemonCreate, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemon = map_create_to_pokemon(pokemon_create)
    pokemon_creado = repo.create_pokemon(pokemon)
    return map_pokemon_to_response(pokemon_creado)


@router.get("/{pokemon_id}", response_model=PokemonResponse)
async def pokemon_por_id(pokemon_id: int, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemon_encontrado = repo.get_pokemon(pokemon_id)
    if not pokemon_encontrado:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    return map_pokemon_to_response(pokemon_encontrado)

@router.delete("/{pokemon_id}", status_code=204)
async def borrar_pokemon(pokemon_id: int, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemon_encontrado = repo.get_pokemon(pokemon_id)
    if not pokemon_encontrado:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    repo.delete_pokemon(pokemon_id)
    return None


@router.patch("/{pokemon_id}", response_model=Pokemon)
async def cambia_pokemon(pokemon_id: int, pokemon: Pokemon, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemon_encontrado = repo.get_pokemon(pokemon_id)
    if not pokemon_encontrado:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    pokemon_data = pokemon.model_dump(exclude_unset=True)
    pokemon_encontrado.sqlmodel_update(pokemon_data)
    repo.update_pokemon(pokemon_encontrado.id, pokemon_data)
    return pokemon_encontrado

@router.put("/", response_model=Pokemon)
async def cambia_pokemon(pokemon: Pokemon, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemon_encontrado = repo.get_pokemon(pokemon.id)
    if not pokemon_encontrado:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    pokemon_data = pokemon.model_dump()
    pokemon_encontrado.sqlmodel_update(pokemon_data)
    repo.update_pokemon(pokemon_encontrado.id, pokemon_data)
    return pokemon_encontrado