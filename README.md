# Simple Summarizer Pipeline

一個簡單的文字摘要 Pipeline，以非同步方式處理輸入文字並回傳摘要結果。採用低耦合設計，摘要邏輯與 Pipeline 執行流程分離，方便替換演算法或撰寫測試。

## 專案結構

```
pipeline.py                        # Open WebUI 載入的進入點（薄封裝層）
openwebui_pipeline/
├── __init__.py                    # 對外匯出 SummarizerPipeline
├── config.py                      # Valves：可調整參數（如摘要長度）
├── summarizers.py                 # Summarizer 策略介面與 TruncateSummarizer 實作
└── core.py                        # SummarizerPipeline：組裝 config 與 summarizer
tests/
├── test_summarizers.py            # 摘要策略單元測試
└── test_pipeline.py               # Pipeline 整合測試
```

- `Summarizer` 是抽象介面，`TruncateSummarizer` 是預設實作（擷取前 N 字元）。
- `SummarizerPipeline` 透過依賴注入接收 `Valves`（設定）與 `Summarizer`（策略），不綁定特定摘要演算法。
- 根目錄的 `pipeline.py` 只負責提供 Open WebUI 需要的 `Pipeline` 類別，實際邏輯委派給 `openwebui_pipeline` 套件。

## 功能

- 接受任意字串輸入
- 預設擷取前 100 個字元作為摘要輸出（可透過 `Valves(max_summary_length=...)` 調整）
- 基於 Python `asyncio` 實作非同步執行
- 摘要演算法可透過注入自訂 `Summarizer` 替換，無需修改 Pipeline 本身

## 使用方式

直接執行腳本：

```bash
python pipeline.py
```

或在程式中引用：

```python
import asyncio
from pipeline import Pipeline

pipeline = Pipeline()
result = asyncio.run(pipeline.run("your input text here"))
print(result)
# Output: {'output': 'Summary: your input text here...'}
```

### 自訂設定與摘要策略

```python
import asyncio
from openwebui_pipeline import SummarizerPipeline
from openwebui_pipeline.config import Valves
from openwebui_pipeline.summarizers import Summarizer

pipeline = SummarizerPipeline(valves=Valves(max_summary_length=20))
result = asyncio.run(pipeline.run("your input text here"))

# 或注入自訂摘要策略
class UppercaseSummarizer(Summarizer):
    def summarize(self, text: str) -> str:
        return text.upper()

pipeline = SummarizerPipeline(summarizer=UppercaseSummarizer())
```

## 輸出格式

```json
{
  "output": "Summary: <前100字元>..."
}
```

## 測試

```bash
python -m pytest
```

## 需求

- Python 3.10+（使用 `dataclass` 與 `X | None` 型別語法）
- 開發測試需要 `pytest`
