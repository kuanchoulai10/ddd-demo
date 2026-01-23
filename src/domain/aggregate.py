"""Domain-Driven Design: Aggregate Root abstract base class."""
from abc import ABC
from typing import List
from .entity import Entity


class AggregateRoot(Entity, ABC):
    """
    Abstract base class for DDD Aggregate Roots.

    An Aggregate is a cluster of domain objects that can be treated as a single unit.
    The Aggregate Root is the only member of the Aggregate that outside objects are
    allowed to hold references to. It ensures consistency and enforces invariants
    within the aggregate boundary.
    """

    def __init__(self):
        self._domain_events: List[Any] = []

    def get_domain_events(self) -> List[Any]:
        """
        Get all domain events that have been raised by this aggregate.

        Returns:
            List[Any]: List of domain events
        """
        return self._domain_events.copy()

    def clear_domain_events(self) -> None:
        """Clear all domain events from this aggregate."""
        self._domain_events.clear()

    def _raise_event(self, event: Any) -> None:
        """
        Raise a domain event.

        Args:
            event: The domain event to raise
        """
        self._domain_events.append(event)
