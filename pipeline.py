import asyncio

from openwebui_pipeline import SummarizerPipeline


class Pipeline:
    """Open WebUI entry point. Delegates all logic to SummarizerPipeline."""

    def __init__(self):
        self.name = "Simple Summarizer Pipeline"
        self._impl = SummarizerPipeline()

    async def run(self, input_text: str) -> dict:
        return await self._impl.run(input_text)


if __name__ == "__main__":
    pipeline = Pipeline()

    test_input = "Cybersecurity systems generate large amounts of data, making it difficult for analysts to identify potential threats."

    result = asyncio.run(pipeline.run(test_input))

    print("Input:", test_input)
    print("Output:", result)
