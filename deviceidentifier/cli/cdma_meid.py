#!/usr/bin/env python
from deviceidentifier import api

import sys, json


def main():
    # Sample showing how to look up data from a CDMA MEID.

    if len(sys.argv) < 2:
        print 'Usage: provide a CDMA MEID for a breakdown of data on it.'
        exit(-1)

    print json.dumps(
        api.lookup( api.TYPE_CDMA_MEID, sys.argv[1:][0] ),
        indent=4, sort_keys=True, ensure_ascii=False, encoding='utf8'
    )

if __name__ == '__main__':
    main()
