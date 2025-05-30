# Standard imports
from unittest.mock import Mock, patch

# Third party imports
import pytest

# Local imports
from conaudio.errors import (
    FFmpegNotInstalledError
)
from conaudio.utils.ffmpeg_utils import (
    verify_ffmpeg_installation
)


def _assert_subprocess_run_called_correctly(mock_run):
    mock_run.assert_called_once_with(
        ["ffmpeg", "-version"],
        capture_output=True,
        text=True,
        check=True
    )


@patch("subprocess.run")
def test_verify_ffmpeg_installation_success(mock_run):
    """Test that verify_ffmpeg_installation passes when ffmpeg is available."""
    mock_run.return_value = Mock(returncode=0)
    verify_ffmpeg_installation()

    _assert_subprocess_run_called_correctly(mock_run)


@patch("subprocess.run", side_effect=Exception("ffmpeg not found"))
def test_verify_ffmpeg_installation_failure(mock_run):
    """Test that verify_ffmpeg_installation raises an FFmpegNotFoundError when
    ffmpeg is unavailable."""
    with pytest.raises(FFmpegNotInstalledError):
        verify_ffmpeg_installation()

    _assert_subprocess_run_called_correctly(mock_run)
