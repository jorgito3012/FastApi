from sqlmodel import Session, select
from models.pokemon import Pokemon

class PokemonsRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_pokemons(self) -> list[Pokemon]:
        pokemons = self.session.exec(select(Pokemon)).all()
        return pokemons

    def get_pokemon(self, pokemon_id: int) -> Pokemon:
        pokemon = self.session.get(Pokemon, pokemon_id)
        return pokemon

    def create_pokemon(self, pokemon: Pokemon) -> Pokemon:
        self.session.add(pokemon)
        self.session.commit()
        self.session.refresh(pokemon)
        return pokemon

    def update_pokemon(self, pokemon_id: int, pokemon_data: dict) -> Pokemon:
        pokemon = self.get_pokemon(pokemon_id)
        for key, value in pokemon_data.items():
            setattr(pokemon, key, value)
        self.session.commit()
        self.session.refresh(pokemon)
        return pokemon

    def delete_pokemon(self, pokemon_id: int) -> None:
        pokemon = self.get_pokemon(pokemon_id)
        self.session.delete(pokemon)
        self.session.commit()
