from typing import Optional


class InternalException(Exception):
    def __init__(self, message: Optional[str], status_code: int) -> None:
        self.message = message
        self.status_code = status_code


class NotFoundException(InternalException):
    """Exception raised when a resource is not found."""

    def __init__(self, resource_name: str, resource_id: int):
        self.resource_name = resource_name
        self.resource_id = resource_id
        message = f"{resource_name} with ID {resource_id} not found"
        super().__init__(message=message, status_code=404)


class ConflictException(InternalException):
    """Exception raised when a resource is not found."""

    def __init__(self, error_message: str):
        super().__init__(message=error_message, status_code=409)
