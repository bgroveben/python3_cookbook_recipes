class HttpException(Exception):

    # -> https://www.python.org/dev/peps/pep-3107/
    def __init__(self, message, code=500) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
