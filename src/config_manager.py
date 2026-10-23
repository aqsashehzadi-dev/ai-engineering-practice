import json
from pathlib import Path
import os
import tempfile


class ConfigurationError(Exception):
    """Raised when configuration is invalid or unreadable."""
    pass


def save_config(config, filename):
    if not isinstance(config, dict):
        raise TypeError("Configuration must be a dictionary.")

    validate_config(config)

    path = Path(filename)

    try:
        write_json_atomically(config, path)

    except (OSError, TypeError, ValueError) as error:
        raise ConfigurationError(
            "Failed to save configuration."
        ) from error

    return path


def load_config(filename):
    path = Path(filename)

    try:
        with path.open("r", encoding="utf-8") as file:
            config = json.load(file)

    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ConfigurationError(
            "Failed to load configuration."
        ) from error

    if not isinstance(config, dict):
        raise ConfigurationError(
            "Configuration must contain a JSON object."
        )

    return validate_config(config)

def validate_config(config):
    if not isinstance(config, dict):
        raise ConfigurationError(
            "Configuration must be a dictionary."
        )

    model = config.get("model")
    temperature = config.get("temperature")
    max_tokens = config.get("max_tokens")

    if not isinstance(model, str) or not model.strip():
        raise ConfigurationError(
            "Model must be a non-empty string."
        )

    if (
        type(temperature) not in (int, float)
        or not 0.0 <= temperature <= 2.0
    ):
        raise ConfigurationError(
            "Temperature must be between 0.0 and 2.0."
        )

    if type(max_tokens) is not int or max_tokens <= 0:
        raise ConfigurationError(
            "max_tokens must be a positive integer."
        )

    return config

def write_json_atomically(config, filename):
    path = Path(filename)
    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            suffix=".tmp",
            delete=False,
        ) as temp_file:
            temp_path = Path(temp_file.name)
            json.dump(config, temp_file, indent=4)
            temp_file.flush()
            os.fsync(temp_file.fileno())

        os.replace(temp_path, path)

    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)