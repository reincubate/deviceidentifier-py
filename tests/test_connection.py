from deviceidentifier.util.exceptions import BadTokenError, MissingTokenError
from deviceidentifier import api

import pytest, os


TEST_SERIALS = {
    'legacy': [ # 80s / 90s legacy, variable length
        'E14029GM1542',
        'F4412SAM0001', # Early 128k Mac
        'C6310ROM0001AP', # Mac Plus. The "O" in this should be a zero but we handle that.
    ],
    'old': [ # Late 90s onwards, the 11-digit format
        '84021NCV3NP',
    ],
    '2010': [ # 2010 onwards, the 12-digit format
        'DQGKX45LF8GL',
    ]
}

class TestConnection(object):

    def test_serials(self):

        if not 'RI_DEVID_TOKEN' in os.environ:
            pytest.skip( 'RI_DEVID_TOKEN API token environment variable not set; you must provde an API token' )

        for serialType in TEST_SERIALS.keys():
            for serialNumber in TEST_SERIALS[serialType]:
                api.query( os.environ['RI_DEVID_TOKEN'], apple_serial=serialNumber )
