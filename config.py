from pydantic import BaseSettings
from typing import List


class ProdConfig(BaseSettings):
    environment: str = "production"
    postgres_host: str = "localhost"
    postgres_port: str = "5432"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db_name: str = "dbname"
    logs_dir: str = "logs"

class DevConfig(BaseSettings):
    environment: str = "develop"
    postgres_host: str = "localhost"
    postgres_port: str = "5432"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db_name: str = "dbname"
    logs_dir: str = "logs"

class TestsConfig(BaseSettings):
    environment: str = "tests"
    postgres_host: str = "localhost"
    postgres_port: str = "5432"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db_name: str = "dbname"
    logs_dir: str = "logs"
