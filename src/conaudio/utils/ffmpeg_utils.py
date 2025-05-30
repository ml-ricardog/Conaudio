# Standard imports
import subprocess

# Local imports
from conaudio.errors import FFmpegNotInstalledError


def verify_ffmpeg_installation() -> None:
    """Verify that ffmpeg is installed and available in the system PATH.

    Raises:
        FFmpegNotInstalledError: If ffmpeg is not installed or cannot be found.
    """
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            check=True
        )
    except Exception as e:
        raise FFmpegNotInstalledError from e
