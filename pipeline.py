class Pipeline:
    def __init__(self):
        self.name = "Simple Summarizer Pipeline"

    async def run(self, input_text: str):
        # 簡單處理：回傳前100字當摘要
        summary = input_text[:100]
        return {
            "output": f"Summary: {summary}..."
        }