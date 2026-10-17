
import json
from pathlib import Path


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = None

        return cls._instance

    def _load_config(self):
        if self._config is None:
            config_path = Path(__file__).resolve().parent.parent / "config.json"

            if not config_path.exists():
                raise FileNotFoundError(
                    f"Configuration file not found: {config_path}"
                )

            with config_path.open("r", encoding="utf-8") as file:
                self._config = json.load(file)

        return self._config

    def get(self, key):
        config = self._load_config()

        if key not in config:
            raise KeyError(f"Configuration key not found: {key}")

        return config[key]