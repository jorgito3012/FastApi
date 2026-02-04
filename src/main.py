from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select

from models.pokemon import Pokemon, PokemonCreate, PokemonResponse,  map_pokemon_to_response, map_create_to_pokemon
from data.db import init_db, get_session
from data.pokemons_repository import PokemonsRepository
from routers.api_pokemons_router import router as api_pokemons_router

import uvicorn

@asynccontextmanager
async def lifespan(application: FastAPI):
    init_db()
    yield

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(api_pokemons_router)

# Ruta para la página principal
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})   

@app.get("/pokemons", response_class=HTMLResponse)
async def ver_pokemons(request: Request, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemons = repo.get_all_pokemons()
    return templates.TemplateResponse("pokemons/pokemons.html", {"request": request, "pokemons": pokemons})

@app.get("/pokemons/new", response_class=HTMLResponse)
async def nuevo_pokemon_form(request: Request):

    """Formulario para añadir un pokemon nuevo"""
    return templates.TemplateResponse("pokemons/pokemon_form.html", {
        "request": request,
        "pokemon": Pokemon()
    })

@app.post("/pokemons/new", response_class=HTMLResponse)
async def crear_pokemon(request: Request, session: SessionDep):
    """Crear un nuevo pokemon desde el formulario"""
    form_data = await request.form()
    nombre = form_data.get("nombre")
    nivel = form_data.get("nivel")
    ataque = form_data.get("ataque")
    defensa = form_data.get("defensa")

    pokemon_create = PokemonCreate(
        nombre=nombre,
        nivel=int(nivel),
        ataque=int(ataque),
        defensa=int(defensa)
    )
    repo = PokemonsRepository(session)
    pokemon = map_create_to_pokemon(pokemon_create)
    repo.create_pokemon(pokemon)

    return RedirectResponse(url="/pokemons", status_code=303)

@app.get("/pokemons/{pokemon_id}", response_class=HTMLResponse)
async def pokemon_por_id(pokemon_id: int, request: Request, session: SessionDep):
    repo = PokemonsRepository(session)
    pokemon_encontrado = repo.get_pokemon(pokemon_id)
    if not pokemon_encontrado:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    pokemon_response = map_pokemon_to_response(pokemon_encontrado)
    return templates.TemplateResponse("pokemons/pokemon_detalle.html", {"request": request, "pokemon": pokemon_response})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)