"""Ping CRM app dev config."""

import os
from app import config


# openssl rand -hex 32
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = config("SECRET_KEY", "__GENERATE_AND_ADD_TO_ENV_FILE__")
SQLALCHEMY_DATABASE_URI = (
    f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}/test.db"
)
INERTIA_TEMPLATE = "base.html"
ITEMS_PER_PAGE = 10
MEDIA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "media")
SESSION_TYPE = "filesystem"
SESSION_FILE_DIR = f"{os.path.abspath(os.path.dirname(__file__))}/sessions"
