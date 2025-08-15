import os
from pathlib import Path
from dotenv import load_dotenv

def load_env(dotenv_path: str | None = None) -> None:
    """
    Load environmental variables from a .env file.
    If dotnev_path is None, it loads from the default project root.
    """
    if dotenv_path is None:
        dotenv_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path)

def get_key(key: str, *, required: bool = True, default: str | None = None) -> str | None:
    """
    Fectch a key from environemnt variables with optional requirement.
    """
    val = os.getenv(key, default)
    if required and val is None:
        raise KeyError(f"Missing required env var: {key}")
    return val

def data_dir() -> Path:
    """
    Retuen the data directory as a Path object.
    """
    return Path(get_key("DATA_DIR", required=False, default="./data"))
