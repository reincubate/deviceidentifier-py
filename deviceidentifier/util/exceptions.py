import json

# Valid error types
ERROR_INVALID_IDENTIFIER = 'invalid_identifier'
ERROR_INVALID_TOKEN = 'invalid_token'
ERROR_EXPIRED_TOKEN = 'expired_token'
ERROR_BAD_REQUEST = 'bad_request'
ERROR_UNHANDLED_ERROR = 'unhandled_error'

# You shouldn't see these
ERROR_PERMISSION_DENIED = 'permission_denied'
ERROR_PAGE_NOT_FOUND = 'page_not_found'


class InvalidIdentifierError(Exception):
    def __init__(self, message):
        super(InvalidIdentifierError, self).__init__(message)
        self.message = message

class InvalidTokenError(Exception):
    def __init__(self, message):
        super(InvalidTokenError, self).__init__(message)
        self.message = message

class ExpiredTokenError(Exception):
    def __init__(self, message):
        super(ExpiredTokenError, self).__init__(message)
        self.message = message

class BadRequestError(Exception):
    def __init__(self, message):
        super(BadRequestError, self).__init__(message)
        self.message = message

class UnhandledError(Exception):
    def __init__(self, message):
        super(UnhandledError, self).__init__(message)
        self.message = message

ERROR_MAPPING = {
    ERROR_INVALID_IDENTIFIER: InvalidIdentifierError,
    ERROR_INVALID_TOKEN: InvalidTokenError,
    ERROR_EXPIRED_TOKEN: ExpiredTokenError,
    ERROR_BAD_REQUEST: BadRequestError,
    ERROR_UNHANDLED_ERROR: UnhandledError,
}

def get_error( error_json, status_code ):
    error_json = json.loads( error_json )

    type, message = error_json['type'], error_json['message']

    if type not in ERROR_MAPPING.keys(): # Uh-oh
        return Exception( '%s (HTTP %s)' % ( message, status_code ) )

    return ERROR_MAPPING[type](message)
