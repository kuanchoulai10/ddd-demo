"""Customer application: DTOs (Data Transfer Objects)."""
from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateCustomerRequest:
    """Request DTO for creating a customer."""
    first_name: str
    last_name: str
    email: str


@dataclass
class CustomerResponse:
    """Response DTO for customer operations."""
    customer_id: UUID
    first_name: str
    last_name: str
    email: str
