# Project: webapp
# File: \config.py
# Created at: Thursday, November 14th 2019, 13:36:12 +03:00
# Author: Tamara A. Repina (4ertovo4ka@gmail.com)
# -----
# Last Modified: Monday, September 23rd 2024, 18:50:55 +03:00
# Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
# Last version: <<projectversion>>
# -----
# Copyright 2024 Tamara A. Repina


from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    ENVIRONMENT: str = "development"
    FLASK_APP: str = "webapp"
    DEBUG: bool = True
    SECRET_KEY: str = "12345678901234567890123456789012"
    # DB
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "1234"
    DB_NAME: str = "vkr_db"
    # SQL
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    model_config = SettingsConfigDict(env_file='.env')


@lru_cache()
def get_settings() -> CoreSettings:
    return CoreSettings()
