"""Domain-Driven Design: Domain Event abstract base class."""
from abc import ABC
from datetime import datetime
from typing import Any


class DomainEvent(ABC):
    """
    Abstract base class for DDD Domain Events.

    Domain Events are used to capture occurrences of something that happened
    in the domain. They represent state changes and are immutable.
    """

    def __init__(self):
        self.occurred_on = datetime.utcnow()

    def __eq__(self, other: Any) -> bool:
        """
        Domain events are equal if they have the same type and attributes.

        Args:
            other: The other object to compare with

        Returns:
            bool: True if events are equal
        """
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__
