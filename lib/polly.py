from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from lib.utils import write_bytes_file


class PollyClient:
    def __init__(self, profile_name):
        self._session = Session(profile_name=profile_name)
        self.Client = self._session.client("polly")

    def synthesize_and_store(self, value, path, voiceId="Joanna", outputFormat="mp3"):
        try:
            res = self.Client.synthesize_speech(
                Text=value,
                VoiceId=voiceId,
                OutputFormat=outputFormat,
            )
            if "AudioStream" in res:
                write_bytes_file(res["AudioStream"], path)
            return res
        except (BotoCoreError, ClientError) as error:
            print(error)
            raise error
