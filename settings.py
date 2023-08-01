import os
from collections import ChainMap
from decouple import Config, RepositoryEnv, AutoConfig


DOTENV_FILE = os.environ.get("DOTENV_FILE", ".env")
SECRETS_FILE = os.environ.get("SECRETS_FILE", ".secrets")

try:
    config = Config(
        ChainMap(
            RepositoryEnv(DOTENV_FILE),
            RepositoryEnv(SECRETS_FILE),
        )
    )
except FileNotFoundError:
    print("Modify environment variables using .env and .secrets files.")
    config = AutoConfig()
