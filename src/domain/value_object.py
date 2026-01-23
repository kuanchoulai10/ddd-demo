"""Domain-Driven Design: Value Object abstract base class."""
from abc import ABC
from typing import Any


class ValueObject(ABC):
    """
    Abstract base class for DDD Value Objects.

    Value Objects are immutable objects that are defined by their attributes
    rather than a unique identity. Two value objects with the same attributes
    are considered equal.
    """

    def __eq__(self, other: Any) -> bool:
        """
        Value objects are equal if all their attributes are equal.

        Args:
            other: The other object to compare with

        Returns:
            bool: True if all attributes are equal
        """
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __hash__(self) -> int:
        """
        Hash based on all attributes.

        Returns:
            int: Hash value based on all attributes
        """
        return hash(tuple(sorted(self.__dict__.items())))
