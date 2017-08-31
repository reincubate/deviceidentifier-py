from deviceidentifier.util.exceptions import BadTokenError, MissingTokenError
from deviceidentifier import api

import pytest, os


class TestToken(object):

    def test_token(self):
        ''' Will the API fail if we provide the wrong token? '''
        with pytest.raises(MissingTokenError) as exc_info:
            api.query( None, apple_model='XX' )

        exception_raised = exc_info.value
        #assert exception_raised.message,
