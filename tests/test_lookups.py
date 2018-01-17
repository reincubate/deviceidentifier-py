from deviceidentifier.util.exceptions import InvalidTokenError, ExpiredTokenError, InvalidIdentifierError
from deviceidentifier import api

import pytest


class TestLookups(object):

    def test_auth(self):
        ''' Will the API fail if we provide the wrong token? '''
        with pytest.raises(InvalidTokenError) as exc_info:
            api.lookup( api.TYPE_APPLE_IDENTIFIER, 'iPhone5,3', token='bad_token', )
        with pytest.raises(ExpiredTokenError) as exc_info:
            api.lookup( api.TYPE_APPLE_IDENTIFIER, 'iPhone5,3', token='yneektgqk98bercl4w5a92wb7kkxe3rh', )

    def test_misformed(self):
        with pytest.raises(InvalidIdentifierError) as exc_info:
            api.lookup( api.TYPE_APPLE_SERIAL, 'XXBADSERIALXX', )

    def test_calls(self):
        api.lookup( api.TYPE_APPLE_ANUMBER,         'A1784', )
        api.lookup( api.TYPE_APPLE_IDENTIFIER,      'iPhone5,3', )
        api.lookup( api.TYPE_APPLE_IDFA,            '002ebf12-a125-5ddf-a739-67c3c5d20177', )
        api.lookup( api.TYPE_APPLE_INTERNAL_NAME,   'N92AP', )
        api.lookup( api.TYPE_APPLE_MODEL,           'MC605FD/A', )
        api.lookup( api.TYPE_APPLE_SERIAL,          'C8QH6T96DPNG', )
        api.lookup( api.TYPE_APPLE_UDID,            'db72cb76a00cb81675f19907d4ac2b298628d83c', )
        api.lookup( api.TYPE_CDMA_MEID,             '354403064522046', )
        api.lookup( api.TYPE_GSMA_ICCID,            '8965880812100011146', )
        api.lookup( api.TYPE_GSMA_IMEI,             '013554006297015', )
        api.lookup( api.TYPE_GSMA_TAC,              '01326300', )
