
import json
from pathlib import Path


class ConfigReader:
    DEFAULT_CONFIG_PATH = (
        Path(__file__).resolve().parent.parent / "config.json"
    )

    _instances = {}

    def __new__(cls, file_path=None):
        if file_path is None:
            path = cls.DEFAULT_CONFIG_PATH
        else:
            path = Path(file_path).resolve()

        path = Path(path).resolve()

        if path not in cls._instances:
            instance = super().__new__(cls)
            instance._config = None
            instance._file_path = path
            cls._instances[path] = instance

        return cls._instances[path]

    def _load_config(self):
        if self._config is None:
            if not self._file_path.exists():
                raise FileNotFoundError(
                    f"Configuration file not found: {self._file_path}"
                )

            with self._file_path.open("r", encoding="utf-8") as file:
                self._config = json.load(file)

        return self._config

    def get(self, key):
        config = self._load_config()

        if key not in config:
            raise KeyError(f"Configuration key not found: {key}")

        return config[key]
