from deviceidentifier.util.exceptions import InvalidTokenError, ExpiredTokenError, InvalidIdentifierError, BadRequestError
from deviceidentifier import api

import pytest


class TestEnhanceMetadata(object):

    def test_auth(self):
        ''' Will the API fail if we provide the wrong token? '''
        with pytest.raises(InvalidTokenError) as exc_info:
            api.enhance_metadata( apple_identifier='iPhone5,3', token='bad_token', )
        with pytest.raises(ExpiredTokenError) as exc_info:
            api.enhance_metadata( apple_identifier='iPhone5,3', token='yneektgqk98bercl4w5a92wb7kkxe3rh', )

    def test_misformed(self):
        with pytest.raises(InvalidIdentifierError) as exc_info:
            api.enhance_metadata( apple_serial='XXBADSERIALXX', )

        with pytest.raises(BadRequestError) as exc_info:
            api.enhance_metadata( apple_serial=None, )

    def test_calls(self):
        api.enhance_metadata(
            apple_anumber='A1784', apple_identifier='iPhone5,3', apple_idfa='002ebf12-a125-5ddf-a739-67c3c5d20177',
            apple_internal_name='N92AP', apple_model='MC605FD/A', apple_serial='C8QH6T96DPNG',
            apple_udid='db72cb76a00cb81675f19907d4ac2b298628d83c',
            cdma_meid='354403064522046',
            gsma_imei='013554006297015', gsma_iccid='8965880812100011146', gsma_tac='01326300',
        )
