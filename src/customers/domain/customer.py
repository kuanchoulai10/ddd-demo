"""Customer domain: Customer aggregate root."""
from typing import Any
from uuid import UUID, uuid4
from domain.aggregate import AggregateRoot
from .value_objects import Email, CustomerName
from .events import CustomerCreatedEvent, CustomerEmailUpdatedEvent


class Customer(AggregateRoot):
    """Customer aggregate root."""

    def __init__(
        self,
        customer_id: UUID,
        name: CustomerName,
        email: Email
    ):
        super().__init__()
        self._customer_id = customer_id
        self._name = name
        self._email = email

    @classmethod
    def create(cls, first_name: str, last_name: str, email: str) -> 'Customer':
        """
        Factory method to create a new customer.

        Args:
            first_name: Customer's first name
            last_name: Customer's last name
            email: Customer's email address

        Returns:
            Customer: New customer instance
        """
        customer_id = uuid4()
        name = CustomerName(first_name, last_name)
        email_vo = Email(email)

        customer = cls(customer_id, name, email_vo)
        customer._raise_event(CustomerCreatedEvent(customer_id, email))

        return customer

    @property
    def customer_id(self) -> UUID:
        """Get customer ID."""
        return self._customer_id

    @property
    def name(self) -> CustomerName:
        """Get customer name."""
        return self._name

    @property
    def email(self) -> Email:
        """Get customer email."""
        return self._email

    def update_email(self, new_email: str) -> None:
        """
        Update customer email.

        Args:
            new_email: New email address
        """
        email_vo = Email(new_email)
        self._email = email_vo
        self._raise_event(CustomerEmailUpdatedEvent(self._customer_id, new_email))

    def __eq__(self, other: Any) -> bool:
        """Customers are equal if they have the same ID."""
        if not isinstance(other, Customer):
            return False
        return self._customer_id == other._customer_id

    def __hash__(self) -> int:
        """Hash based on customer ID."""
        return hash(self._customer_id)
