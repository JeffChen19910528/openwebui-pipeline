from openwebui_pipeline.summarizers import TruncateSummarizer


def test_truncate_summarizer_cuts_at_max_length():
    summarizer = TruncateSummarizer(max_length=5)
    assert summarizer.summarize("abcdefgh") == "abcde..."


def test_truncate_summarizer_keeps_short_text_whole():
    summarizer = TruncateSummarizer(max_length=100)
    assert summarizer.summarize("short") == "short..."


def test_truncate_summarizer_default_length_is_100():
    summarizer = TruncateSummarizer()
    text = "a" * 150
    assert summarizer.summarize(text) == "a" * 100 + "..."
