#!/usr/bin/env python
from deviceidentifier import api

import sys, json


def main():
    # Look at what we can get with the identifiers from an iTunes backup.

    if len(sys.argv) != 6:
        print 'Usage: provide an identifier, a serial number, an internal name, an IMEI and an ICCID'
        print 'Try: iPhone5,3 C8QH6T96DPNG N92AP 013554006297015 8965880812100011146'
        exit(-1)

    identifierCode = sys.argv[1:][0]
    serialNumber = sys.argv[1:][1]
    internalName = sys.argv[1:][2]
    imeiCode = sys.argv[1:][3]
    iccidCode = sys.argv[1:][4]

    print json.dumps(
        api.enhance_metadata(
            apple_identifier=identifierCode,
            apple_serial=serialNumber,
            gsma_imei=imeiCode,
            gsma_iccid=iccidCode,
        ),
        indent=4, sort_keys=True, ensure_ascii=False, encoding='utf8'
    )

if __name__ == '__main__':
    main()
