from hashlib import sha256
from datetime import datetime

class ContextJournal:
    def __init__(self):
        self.kernel = {}
        self.boot = {}
        self.loaded_at = datetime.utcnow().isoformat() + "Z"

    def load_kernel(self, data: dict):
        self.kernel = data or {}
        self._validate_kernel()

    def load_boot(self, data: dict):
        self.boot = data or {}
        self._validate_boot()

    def validate(self) -> bool:
        return bool(self.kernel) and bool(self.boot)

    def snapshot(self) -> dict:
        return {
            "kernel": self.kernel,
            "boot": self.boot,
            "loaded_at": self.loaded_at
        }

    def hash(self) -> str:
        raw = repr(self.snapshot()).encode("utf-8")
        return sha256(raw).hexdigest()

    def _validate_kernel(self):
        required = ["ethos", "authority", "stop_conditions"]
        for k in required:
            if k not in self.kernel:
                raise RuntimeError(f"Missing kernel context: {k}")

    def _validate_boot(self):
        required = ["primary_goal", "mode", "priorities", "scope"]
        for k in required:
            if k not in self.boot:
                raise RuntimeError(f"Missing boot context: {k}")
