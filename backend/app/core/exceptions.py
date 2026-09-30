from fastapi import HTTPException, status

class AppException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ResourceNotFoundException(AppException):
    def __init__(self, message: str = "Requested resource not found"):
        super().__init__(message, status_code=status.HTTP_404_NOT_FOUND)

class ActionValidationException(AppException):
    def __init__(self, message: str = "Invalid action parameters"):
        super().__init__(message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ProviderExecutionException(AppException):
    def __init__(self, message: str = "LLM Provider execution error"):
        super().__init__(message, status_code=status.HTTP_502_BAD_GATEWAY)
