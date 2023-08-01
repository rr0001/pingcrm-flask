"""Ping CRM app prod config."""

import os
from settings import config


# openssl rand -hex 20
SECRET_KEY = config('SECRET_KEY', 'PLEASEUPDATEUSINGCOMMANDABOVE')
SQLALCHEMY_DATABASE_URI = (
    f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}/app.db"
)
INERTIA_TEMPLATE = "base.html"
ITEMS_PER_PAGE = 10
MEDIA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "media")
SESSION_TYPE = "filesystem"
SESSION_FILE_DIR = f"{os.path.abspath(os.path.dirname(__file__))}/sessions"
