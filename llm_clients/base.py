from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class LLMResult:
    text: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float


class BaseLLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> LLMResult:
        ...
