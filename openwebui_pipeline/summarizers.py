from abc import ABC, abstractmethod


class Summarizer(ABC):
    """Strategy interface for producing a summary from input text."""

    @abstractmethod
    def summarize(self, text: str) -> str:
        raise NotImplementedError


class TruncateSummarizer(Summarizer):
    """Summarizes by truncating the input to a fixed character length."""

    def __init__(self, max_length: int = 100):
        self.max_length = max_length

    def summarize(self, text: str) -> str:
        return f"{text[: self.max_length]}..."
