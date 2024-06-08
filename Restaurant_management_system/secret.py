import random
from uuid import uuid4
from datetime import datetime, timedelta
import os
import json

"""
Generates a unique secret key every 24hrs, custom though
"""


def generate_unique_string():
    return (
        str(int(uuid4()) * 3)
        + "".join(chr(random.randint(32, 126)) for _ in range(4))
        + datetime.now().strftime("%Y%m%d")
    )


def get_unique_string():
    file_path = os.path.join(os.path.dirname(__file__), "unique_string.json")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            last_generated = datetime.fromisoformat(data["timestamp"])
            if datetime.now() - last_generated < timedelta(days=1):
                return data["unique_string"]

    unique_string = generate_unique_string()
    with open(file_path, "w") as file:
        json.dump(
            {"unique_string": unique_string, "timestamp": datetime.now().isoformat()},
            file,
        )

    return unique_string


UNIQUE_STRING = get_unique_string()
