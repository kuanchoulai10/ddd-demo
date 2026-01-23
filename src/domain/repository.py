"""Domain-Driven Design: Repository port (interface) abstract base class."""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')


class Repository(ABC, Generic[T]):
    """
    Abstract base class for DDD Repository (Port).

    A Repository is a port (interface) that provides the illusion of an in-memory
    collection of all objects of a certain type. It mediates between the domain
    and data mapping layers using a collection-like interface for accessing
    domain objects.

    This is a Port in the Ports and Adapters (Hexagonal) architecture.
    """

    @abstractmethod
    def add(self, entity: T) -> None:
        """
        Add a new entity to the repository.

        Args:
            entity: The entity to add
        """
        pass

    @abstractmethod
    def get(self, entity_id: any) -> Optional[T]:
        """
        Get an entity by its ID.

        Args:
            entity_id: The unique identifier of the entity

        Returns:
            Optional[T]: The entity if found, None otherwise
        """
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        """
        Update an existing entity.

        Args:
            entity: The entity to update
        """
        pass

    @abstractmethod
    def delete(self, entity_id: any) -> None:
        """
        Delete an entity by its ID.

        Args:
            entity_id: The unique identifier of the entity
        """
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """
        Find all entities.

        Returns:
            List[T]: List of all entities
        """
        pass
