from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Paths:
    plane_b: Path
    index: Path
    exports: Path
