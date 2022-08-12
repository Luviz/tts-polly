import argparse


class ArgumentParser:
    def __init__(self):
        self.help = {
            "text": "The value to be processed.",
            "profile": "profile name in your ~/.aws/credentials. the default value is 'default'",
        }

        self.parser = argparse.ArgumentParser(
            description="Text to speech, feed in text get audio file out"
        )

        parser_mode = self.parser.add_argument_group("Mode")

        parser_mode.add_argument(
            "-t",
            "--text",
            help=self.help["text"],
        )

        parser_mode.add_argument(
            "-p",
            "--profile",
            help=self.help["profile"],
            default="default",
        )

    def parse_args(self):
        return self.parser.parse_args()
