import os
from collections import ChainMap
from decouple import Config, RepositoryEnv


DOTENV_FILE = os.environ.get("DOTENV_FILE", ".env")
SECRETS_FILE = os.environ.get("SECRETS_FILE", ".secrets")

config = Config(
    ChainMap(
        RepositoryEnv(DOTENV_FILE),
        RepositoryEnv(SECRETS_FILE),
    )
)
