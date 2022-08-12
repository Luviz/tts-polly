from contextlib import closing
from hashlib import sha256


def hash_value(value: str):
    return sha256(value.encode()).hexdigest()

def write_text_file(value: str, path:str):
    with open(path, "w") as file:
        file.write(value)

def write_bytes_file(value, path:str):
    with closing(value) as stream:
        with open(path, "wb") as file:
            file.write(stream.read())
