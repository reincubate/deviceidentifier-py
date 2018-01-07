from deviceidentifier.util.exceptions import InvalidTokenError, ExpiredTokenError
from deviceidentifier import api

import pytest


class TestIdentifierIdentifiers(object):

    def test_auth(self):
        ''' Will the API fail if we provide the wrong token? '''
        with pytest.raises(InvalidTokenError) as exc_info:
            api.identify_identifier( 'iPhone5,3', token='bad_token', )
        with pytest.raises(ExpiredTokenError) as exc_info:
            api.identify_identifier( 'iPhone5,3', token='yneektgqk98bercl4w5a92wb7kkxe3rh', )

    def test_calls(self):
        api.identify_identifier( 'C8QH6T96DPNG', )
