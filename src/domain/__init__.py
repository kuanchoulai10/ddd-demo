"""Domain-Driven Design abstract base classes."""
from .entity import Entity
from .value_object import ValueObject
from .aggregate import AggregateRoot
from .repository import Repository
from .adapter import Adapter
from .domain_event import DomainEvent

__all__ = [
    'Entity',
    'ValueObject',
    'AggregateRoot',
    'Repository',
    'Adapter',
    'DomainEvent',
]
