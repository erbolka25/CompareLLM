import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from llm_clients.base import BaseLLMClient, LLMResult

load_dotenv()

DEFAULT_MODEL = "gpt-4o-mini"


class OpenAIClient(BaseLLMClient):
    def __init__(self, model: str = DEFAULT_MODEL):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in .env")

        self.model = model
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> LLMResult:
        start = time.perf_counter()
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        latency_ms = (time.perf_counter() - start) * 1000

        return LLMResult(
            text=response.choices[0].message.content,
            model=response.model,
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            latency_ms=latency_ms,
        )
