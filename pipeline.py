import asyncio

class Pipeline:
    def __init__(self):
        self.name = "Simple Summarizer Pipeline"

    async def run(self, input_text: str):
        # 簡單處理：回傳前100字當摘要
        summary = input_text[:100]
        return {
            "output": f"Summary: {summary}..."
        }

if __name__ == "__main__":
    pipeline = Pipeline()
    
    test_input = "Cybersecurity systems generate large amounts of data, making it difficult for analysts to identify potential threats."
    
    result = asyncio.run(pipeline.run(test_input))
    
    print("Input:", test_input)
    print("Output:", result)