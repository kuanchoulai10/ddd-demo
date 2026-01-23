"""Domain-Driven Design: Entity abstract base class."""
from abc import ABC, abstractmethod
from typing import Any


class Entity(ABC):
    """
    Abstract base class for DDD Entities.

    Entities are objects that have a distinct identity that runs through time
    and different representations. They are defined by their identity rather
    than their attributes.
    """

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        """
        Entities are equal if they have the same identity.

        Args:
            other: The other object to compare with

        Returns:
            bool: True if both entities have the same identity
        """
        pass

    @abstractmethod
    def __hash__(self) -> int:
        """
        Hash based on entity identity.

        Returns:
            int: Hash value based on the entity's identity
        """
        pass
