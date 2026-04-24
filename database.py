import os

from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": os.getenv("HOST"),
                "port": os.getenv("PORT"),
                "user": os.getenv("USERNAME"),
                "password": os.getenv("PASSWORD"),
                "database": os.getenv("DB"),
            },
        }
    },
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
