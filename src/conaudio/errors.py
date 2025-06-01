class ConaudioError(Exception):
    """Base class for custom backend exceptions with auto-stored attributes."""

    def __init__(self, message: str, **kwargs) -> None:
        super().__init__(message)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.details = kwargs


class FFmpegNotInstalledError(ConaudioError):
    """Raised when ffmpeg is not installed or cannot be found."""

    def __init__(self) -> None:
        super().__init__("ffmpeg is not installed or cannot be found")


class FFmpegCommandExecutionError(ConaudioError):
    """Raised when ffmpeg fails to run the given command.

    Args:
        command (str): Command that fails to run.
    """

    def __init__(self, command: str) -> None:
        message = f"Failed to run the command: '{command}'"
        super().__init__(message, command=command)
