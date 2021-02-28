"""Set up project paths."""
from pathlib import Path


def project_root() -> Path:
    """Get project path."""
    return Path(__file__).parent.parent


def storage_root() -> Path:
    """Get storage path."""
    return Path(__file__).parent.parent / "storage"


def outputs_root() -> Path:
    """Get output path."""
    path = Path(__file__).parent.parent / "output"
    Path(path).mkdir(exist_ok=True, parents=True)
    return path


# https://stackoverflow.com/a/50194143/1889006
# https://stackoverflow.com/a/53465812/1889006
