"""
CAOS-A1 Smoke Test

Non-destructive.
No writes.
No servers.
"""

from pathlib import Path

from caos_core.kernel import CAOSKernel
from caos_core.paths import Paths


def run():
    paths = Paths(
        plane_b=Path("data/plane_b"),
        index=Path("data/index"),
        exports=Path("data/exports"),
    )

    kernel = CAOSKernel(paths)

    # Explicit recall with no anchors must fail closed
    results = kernel.recall.recall("recall:")
    assert results == [], "Recall without anchors must return empty list"

    print("SMOKE TEST PASSED")


if __name__ == "__main__":
    run()
