from decouple import config as ENV


def get_settings_module() -> str:
    return f"src.settings.{ENV('ENVIRONMENT')}"
