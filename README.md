# Simple Summarizer Pipeline

一個簡單的文字摘要 Pipeline，以非同步方式處理輸入文字並回傳摘要結果。

## 功能

- 接受任意字串輸入
- 擷取前 100 個字元作為摘要輸出
- 基於 Python `asyncio` 實作非同步執行

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

## 輸出格式

```json
{
  "output": "Summary: <前100字元>..."
}
```

## 需求

- Python 3.7+（需支援 `asyncio`）
