from sqlmodel import create_engine, SQLModel, Session
from models.pokemon import Pokemon
import os

db_user: str = os.getenv("DB_USER", "jorge")
db_password: str = os.getenv("DB_PASSWORD", "sasa1234")
db_server: str = os.getenv("DB_SERVER", "fastapi-db")
db_port: int = int(os.getenv("DB_PORT", 5432))
db_name: str = os.getenv("DB_NAME", "pokemonsdb")

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(Pokemon(id=1, nombre="Pikachu", nivel=25, ataque=55, defensa=40))
        session.add(Pokemon(id=2, nombre="Charmander", nivel=12, ataque=52, defensa=43))
        session.add(Pokemon(id=3, nombre="Bulbasaur", nivel=15, ataque=49, defensa=49))
        session.add(Pokemon(id=4, nombre="Squirtle", nivel=18, ataque=48, defensa=65))
        session.add(Pokemon(id=5, nombre="Gengar", nivel=36, ataque=65, defensa=60))
        session.commit()