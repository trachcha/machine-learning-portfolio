"""Small utilities shared across notebooks."""

from pathlib import Path


def project_root() -> Path:
    """Return the project root (parent of src/)."""
    return Path(__file__).resolve().parents[1]


def data_paths() -> dict[str, Path]:
    root = project_root()
    return {
        "raw": root / "data" / "raw",
        "processed": root / "data" / "processed",
        "models": root / "models",
        "figures": root / "reports" / "figures",
    }
