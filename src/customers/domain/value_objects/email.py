"""Customer domain: Email value object."""
import re
from domain.value_object import ValueObject


class Email(ValueObject):
    """Email address value object."""

    def __init__(self, value: str):
        self._validate(value)
        self.value = value

    def _validate(self, value: str) -> None:
        """Validate email format."""
        if not value:
            raise ValueError("Email cannot be empty")

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email format: {value}")

    def __str__(self) -> str:
        return self.value
