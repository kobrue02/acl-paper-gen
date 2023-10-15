import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ['openai_api_key']


class NLGModule:

    def __init__(self) -> None:
        self._system = \
                "You are an expert in Computational Linguistics with a Phd in applied linguistics and computer science." \
                "You have written various scientific papers and are now working on a new paper."

    def _get_response(self, prompt: list[dict[str, str]]) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt
        )
        return response["choices"][0]["message"]["content"]