from dataclasses import dataclass
from pathlib import Path


# Entity - return type of a defined classes
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path