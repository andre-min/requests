class HttpUnprocessableEntityError(Exception):
    '''http Unprocessable error'''
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422
