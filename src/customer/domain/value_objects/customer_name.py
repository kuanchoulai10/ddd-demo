"""Customer domain: CustomerName value object."""
from domain.value_object import ValueObject


class CustomerName(ValueObject):
    """Customer name value object."""

    def __init__(self, first_name: str, last_name: str):
        self._validate(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

    def _validate(self, first_name: str, last_name: str) -> None:
        """Validate customer name."""
        if not first_name or not first_name.strip():
            raise ValueError("First name cannot be empty")
        if not last_name or not last_name.strip():
            raise ValueError("Last name cannot be empty")

    def full_name(self) -> str:
        """Get full name."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()
