from .config import Valves
from .summarizers import Summarizer, TruncateSummarizer


class SummarizerPipeline:
    """Orchestrates text summarization, decoupled from any specific
    summarization strategy via dependency injection."""

    def __init__(self, valves: Valves | None = None, summarizer: Summarizer | None = None):
        self.valves = valves or Valves()
        self.summarizer = summarizer or TruncateSummarizer(self.valves.max_summary_length)

    async def run(self, input_text: str) -> dict:
        summary = self.summarizer.summarize(input_text)
        return {"output": f"Summary: {summary}"}
