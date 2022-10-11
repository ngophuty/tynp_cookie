from pydantic import BaseSettings


class Enviroment(BaseSettings):

    HOST: str
    PORT: int
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: str


env = Enviroment(_env_file ='.env')