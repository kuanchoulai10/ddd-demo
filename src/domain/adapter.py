"""Domain-Driven Design: Adapter abstract base class for Ports and Adapters architecture."""
from abc import ABC


class Adapter(ABC):
    """
    Abstract base class for Adapters in the Ports and Adapters architecture.

    Adapters implement the ports (interfaces) and provide concrete implementations
    that interact with external systems, databases, APIs, etc. They translate
    between the domain model and the outside world.

    Examples of adapters:
    - Database adapters (implementing repository ports)
    - REST API adapters
    - Message queue adapters
    - File system adapters
    """
    pass
