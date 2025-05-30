class ConaudioError(Exception):
    """Base class for custom backend exceptions with auto-stored attributes."""
    def __init__(self, message: str, **kwargs) -> None:
        super().__init__(message)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.details = kwargs
