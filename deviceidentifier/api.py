from deviceidentifier.util.exceptions import BadTokenError, MissingTokenError

import requests
import json


def query(  token, apple_model=None, apple_serial=None, apple_identifier=None,
            gsma_imei=None, gsma_iccid=None, cdma_meid=None ):

    if not token:
        raise MissingTokenError( 'Token not specified; must be provided to authenticate with the API' )

    built_query = {
        'client': {
            'token': token,
        },
        'identifiers': {
        },
    }

    if apple_model:
        built_query['identifiers']['apple_model'] = apple_model

    if apple_serial:
        built_query['identifiers']['apple_serial'] = apple_serial

    if apple_identifier:
        built_query['identifiers']['apple_identifier'] = apple_identifier

    if gsma_imei:
        built_query['identifiers']['gsma_imei'] = gsma_imei

    if gsma_iccid:
        built_query['identifiers']['gsma_iccid'] = gsma_iccid

    if cdma_meid:
        built_query['identifiers']['cdma_meid'] = cdma_meid

    if len( built_query['identifiers'].keys() ) == 0:
        raise Exception( 'No identifiers passed to query' )

    response = requests.post(
        'http://localhost:8000/enhance-metadata/',
        data=json.dumps( built_query )
    )

    if response.status_code != 200:
        if response.headers['Content-Type'] == 'application/json':
            print response.content
            exit(-1)
        raise Exception( 'API call not successful, response code %s:\n%s' % ( response.status_code, response.content ) )

    return json.loads( response.content )
