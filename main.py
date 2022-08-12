import sys
from os import getenv, path

import pathlib
from lib import PollyClient, ArgumentParser, write_text_file, hash_value

parser = ArgumentParser()
args = parser.parse_args()

user_home = getenv("HOME")
root_dir = f"{user_home}/.local/share/tty-polly"
text_dir = f"{root_dir}/text"
audio_dir = f"{root_dir}/audio"


def post_prep():
    pathlib.Path(root_dir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(text_dir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(audio_dir).mkdir(parents=True, exist_ok=True)


def getText():
    text = args.text
    if text is None:
        with sys.stdin as file:
            if not file.isatty():
                text = file.read()
    return text


def main():
    post_prep()
    text = getText()
    profile_name = args.profile
    if text is None:
        print("Could not find any text to process!")
        sys.exit(-1)

    hash_value = hash_value(text)

    text_path = f"{text_dir}/{hash_value}.txt"
    audio_path = f"{audio_dir}/{hash_value}.mp3"

    text_exists = path.exists(text_path)
    audio_exists = path.exists(audio_path)

    if not text_exists:
        write_text_file(text, text_path)

    if not audio_exists:
        polly = PollyClient(profile_name)
        polly.synthesize_and_store(text, audio_path)

    sys.stdout.write(f"{audio_path}")
    return audio_path


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
        sys.exit(-1)
