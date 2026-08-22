import asyncio

from openwebui_pipeline import SummarizerPipeline
from openwebui_pipeline.config import Valves
from openwebui_pipeline.summarizers import Summarizer


class UppercaseSummarizer(Summarizer):
    """Test double proving the pipeline is decoupled from the strategy."""

    def summarize(self, text: str) -> str:
        return text.upper()


def test_run_returns_expected_output_shape():
    pipeline = SummarizerPipeline()
    result = asyncio.run(pipeline.run("hello world"))
    assert result == {"output": "Summary: hello world..."}


def test_run_respects_custom_valves():
    pipeline = SummarizerPipeline(valves=Valves(max_summary_length=3))
    result = asyncio.run(pipeline.run("hello world"))
    assert result == {"output": "Summary: hel..."}


def test_run_uses_injected_summarizer():
    pipeline = SummarizerPipeline(summarizer=UppercaseSummarizer())
    result = asyncio.run(pipeline.run("hello"))
    assert result == {"output": "Summary: HELLO"}
