"""Example: Testing with dependency injection override."""
from fastapi.testclient import TestClient
from unittest.mock import Mock
from uuid import uuid4
from customer.domain.repositories import CustomerRepository
from customer.application.dtos import CustomerResponse
from customer.api.dependencies import get_customer_repository
from app import app


def test_create_customer_with_mock_repository():
    """Example of how dependency injection makes testing easier."""
    # Create a mock repository
    mock_repository = Mock(spec=CustomerRepository)
    mock_repository.find_by_email.return_value = None  # No existing customer

    # Override the dependency
    app.dependency_overrides[get_customer_repository] = lambda: mock_repository

    # Create test client
    client = TestClient(app)

    # Make request
    response = client.post(
        '/api/customers',
        json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        }
    )

    # Verify
    assert response.status_code == 201
    assert mock_repository.find_by_email.called
    assert mock_repository.add.called

    # Clean up
    app.dependency_overrides.clear()
