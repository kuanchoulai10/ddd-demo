"""Customer domain: CustomerRepository port (interface)."""
from abc import abstractmethod
from typing import Optional
from uuid import UUID
from domain.repository import Repository
from ..customer import Customer


class CustomerRepository(Repository[Customer]):
    """
    Customer repository port (interface).

    This is a port in the Ports and Adapters architecture.
    Concrete implementations (adapters) will implement this interface.
    """

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Customer]:
        """
        Find a customer by email address.

        Args:
            email: Email address to search for

        Returns:
            Optional[Customer]: Customer if found, None otherwise
        """
        pass

    @abstractmethod
    def next_identity(self) -> UUID:
        """
        Generate next customer identity.

        Returns:
            UUID: New unique customer ID
        """
        pass
