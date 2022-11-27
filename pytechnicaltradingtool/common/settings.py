import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))


def _get_dotenv_file() -> Path:
    dot_env_file = Path(os.path.join(ROOT_PATH, ".env"))
    default_dot_env_path = Path(os.path.join(os.path.dirname(__file__), ".env"))
    if dot_env_file.is_file():
        return dot_env_file
    else:
        return default_dot_env_path


load_dotenv(_get_dotenv_file())

DATABASE_URL = os.getenv("DATABASE_URL")
