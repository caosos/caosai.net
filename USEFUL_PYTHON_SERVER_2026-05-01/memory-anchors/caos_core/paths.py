from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    """
    Canonical filesystem paths for CAOS-A1.

    This object is inert configuration only.
    """
    plane_b: Path
    index: Path
    exports: Path
