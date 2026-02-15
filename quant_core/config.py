from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class AppConfig:
    db_path: Path = Path("data/quant.db")
    artifacts_dir: Path = Path("artifacts")
    prices_dir: Path = Path("data/sample_prices")
    timezone: str = "Australia/Brisbane"
