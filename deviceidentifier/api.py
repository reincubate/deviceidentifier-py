from deviceidentifier.util.exceptions import BadTokenError, MissingTokenError

import requests
import json


def query(  token, apple_model=None, apple_serial=None, apple_identifier=None,
            apple_internal_name=None, apple_udid=None, apple_anumber=None,
            gsma_imei=None, gsma_tac=None, gsma_iccid=None,
            cdma_meid=None, unknown=None ):

    if not token:
        raise MissingTokenError( 'Token not specified; must be provided to authenticate with the API' )

    built_query = {
        'identifiers': {
        },
    }

    if apple_model:
        built_query['identifiers']['apple_model'] = apple_model

    if apple_serial:
        built_query['identifiers']['apple_serial'] = apple_serial

    if apple_identifier:
        built_query['identifiers']['apple_identifier'] = apple_identifier

    if apple_internal_name:
        built_query['identifiers']['apple_internal_name'] = apple_internal_name

    if apple_udid:
        built_query['identifiers']['apple_udid'] = apple_udid

    if apple_anumber:
        built_query['identifiers']['apple_anumber'] = apple_anumber

    if gsma_imei:
        built_query['identifiers']['gsma_imei'] = gsma_imei

    if gsma_tac:
        built_query['identifiers']['gsma_tac'] = gsma_tac

    if gsma_iccid:
        built_query['identifiers']['gsma_iccid'] = gsma_iccid

    if cdma_meid:
        built_query['identifiers']['cdma_meid'] = cdma_meid

    endpoint = 'enhance-metadata'

    if unknown:
        if len( built_query['identifiers'].keys() ) > 0:
            raise Exception( 'Cannot combine identify request with lookups' )
        built_query['identifiers']['unknown'] = unknown
        endpoint = 'identify-identifier'

    if len( built_query['identifiers'].keys() ) == 0:
        raise Exception( 'No identifiers passed to query' )

    response = requests.post(
        'https://di-api.reincubate.com/%s/' % endpoint,
        data=json.dumps( built_query ),
        headers={ 'Authorization': 'Token %s' % token, },
    )

    if response.status_code != 200:
        if response.headers['Content-Type'] == 'application/json':
            print response.content
            exit(-1)
        raise Exception( 'API call not successful, response code %s:\n%s' % ( response.status_code, response.content ) )

    return json.loads( response.content )
