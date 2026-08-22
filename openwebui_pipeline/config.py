from dataclasses import dataclass


@dataclass(frozen=True)
class Valves:
    """Configurable parameters for the pipeline."""

    max_summary_length: int = 100
