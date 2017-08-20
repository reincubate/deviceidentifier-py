#!/usr/bin/env python
from deviceidentifier.api import query

import os, sys, json

def main():
    # Look at what we can get with the identifiers from an iTunes backup.

    if len(sys.argv) != 6:
        print 'Usage: provide an identifier, a serial number, a model, an IMEI and an ICCID'
        print 'Try: iPhone3,1 5K31926NDZZ N90AP 358686054544170 8965880812100011146'
        exit(-1)

    if not 'RI_DEVID_TOKEN' in os.environ:
        raise Exception( 'RI_DEVID_TOKEN API token environment variable not set; you must provde an API token' )

    # We can also get UDID

    identifierCode = sys.argv[1:][0]
    serialNumber = sys.argv[1:][1]
    modelCode = sys.argv[1:][2]
    imeiCode = sys.argv[1:][3]
    iccidCode = sys.argv[1:][4]

    print json.dumps(
        query(
            os.environ['RI_DEVID_TOKEN'],
            apple_identifier=identifierCode,
            apple_serial=serialNumber,
            gsma_imei=imeiCode,
            gsma_iccid=iccidCode,
        ),
        indent=4
    )

if __name__ == '__main__':
    main()
