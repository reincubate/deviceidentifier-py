from deviceidentifier.util.exceptions import get_error, BadRequestError, InvalidIdentifierError

import requests, json, logging, os

# Get an instance of a logger
logger = logging.getLogger( 'deviceidentifier' )

# Valid identifier types
TYPE_APPLE_ANUMBER = 'apple-anumbers'
TYPE_APPLE_IDENTIFIER = 'apple-identifiers'
TYPE_APPLE_IDFA = 'apple-idfas'
TYPE_APPLE_INTERNAL_NAME = 'apple-internal-names'
TYPE_APPLE_MODEL = 'apple-models'
TYPE_APPLE_SERIAL = 'apple-serials'
TYPE_APPLE_UDID = 'apple-udids'
TYPE_CDMA_MEID = 'cdma-meids'
TYPE_GSMA_ICCID = 'gsma-iccids'
TYPE_GSMA_IMEI = 'gsma-imeis'
TYPE_GSMA_TAC = 'gsma-tacs'

VALID_TYPES = [
    TYPE_APPLE_ANUMBER, TYPE_APPLE_IDENTIFIER, TYPE_APPLE_IDFA,
    TYPE_APPLE_INTERNAL_NAME, TYPE_APPLE_MODEL, TYPE_APPLE_SERIAL,
    TYPE_APPLE_UDID,
    TYPE_CDMA_MEID,
    TYPE_GSMA_ICCID, TYPE_GSMA_IMEI, TYPE_GSMA_TAC,
]

TOKEN_ENV = os.environ.get( 'RI_DEVID_TOKEN', None )


def lookup( type, identifier, token=None, ):
    if not token and TOKEN_ENV:
        token = TOKEN_ENV

    if not token:
        logger.warn( 'Token not specified, relying on anonymous access which may be limited or rate-limited' )
        headers = {}
    else:
        headers = { 'Authorization': 'Token %s' % token, }

    if type not in VALID_TYPES:
        raise InvalidIdentifierError( '"%s" is not a valid identifier type: see VALID_TYPES' % type )

    response = requests.get(
        'https://di-api.reincubate.com/v1/%s/%s/' % ( type, identifier ),
        headers=headers,
    )

    if response.status_code != 200:
        raise get_error( response.content, response.status_code )

    return json.loads( response.content )

def identify_identifier( identifier, token=None, ):
    if not token and TOKEN_ENV:
        token = TOKEN_ENV

    if not token:
        logger.warn( 'Token not specified, relying on anonymous access which may be limited or rate-limited' )
        headers = {}
    else:
        headers = { 'Authorization': 'Token %s' % token, }

    response = requests.get(
        'https://di-api.reincubate.com/v1/identify-identifier/%s/' % identifier,
        headers=headers,
    )

    if response.status_code != 200:
        raise get_error( response.content, response.status_code )

    return json.loads( response.content )

def enhance_metadata( apple_anumber=None, apple_identifier=None, apple_idfa=None,
                      apple_internal_name=None, apple_model=None, apple_serial=None,
                      apple_udid=None,
                      cdma_meid=None,
                      gsma_imei=None, gsma_iccid=None, gsma_tac=None,
                      additional={},
                      token=None, ):
    if not token and TOKEN_ENV:
        token = TOKEN_ENV

    if not token:
        logger.warn( 'Token not specified, relying on anonymous access which may be limited or rate-limited' )
        headers = {}
    else:
        headers = { 'Authorization': 'Token %s' % token, }

    built_query = { 'identifiers': {}, }

    if apple_anumber:
        built_query['identifiers']['apple_anumber'] = apple_anumber
    if apple_identifier:
        built_query['identifiers']['apple_identifier'] = apple_identifier
    if apple_idfa:
        built_query['identifiers']['apple_idfa'] = apple_idfa
    if apple_internal_name:
        built_query['identifiers']['apple_internal_name'] = apple_internal_name
    if apple_model:
        built_query['identifiers']['apple_model'] = apple_model
    if apple_serial:
        built_query['identifiers']['apple_serial'] = apple_serial
    if apple_udid:
        built_query['identifiers']['apple_udid'] = apple_udid

    if cdma_meid:
        built_query['identifiers']['cdma_meid'] = cdma_meid

    if gsma_imei:
        built_query['identifiers']['gsma_imei'] = gsma_imei
    if gsma_iccid:
        built_query['identifiers']['gsma_iccid'] = gsma_iccid
    if gsma_tac:
        built_query['identifiers']['gsma_tac'] = gsma_tac

    if additional:
        built_query['identifiers']['additional'] = additional

    if len( built_query['identifiers'].keys() ) == 0:
        raise BadRequestError( 'No identifiers passed to query' )

    response = requests.post(
        'https://di-api.reincubate.com/v1/enhance-metadata/',
        headers=headers,
        data=json.dumps( built_query ),
    )

    if response.status_code != 200:
        raise get_error( response.content, response.status_code )

    return json.loads( response.content )
