
class MissingTokenError(Exception):
    def __init__(self, message):
        super(MissingTokenError, self).__init__(message)
        self.message = message

class BadTokenError(Exception):
    def __init__(self, message):
        super(BadTokenError, self).__init__(message)
        self.message = message
