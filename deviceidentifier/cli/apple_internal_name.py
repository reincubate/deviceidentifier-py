#!/usr/bin/env python
from deviceidentifier.api import query

import os, sys, json


def main():
    # Sample showing how to look up data from an Apple internal name.

    if len(sys.argv) < 2:
        print 'Usage: provide an Apple internal name for a breakdown of data on it.'
        exit(-1)

    if not 'RI_DEVID_TOKEN' in os.environ:
        raise Exception( 'RI_DEVID_TOKEN API token environment variable not set; you must provde an API token' )

    apple_internal_name = sys.argv[1:][0]
    print json.dumps( query( os.environ['RI_DEVID_TOKEN'], apple_internal_name=apple_internal_name ), indent=4 )

if __name__ == '__main__':
    main()
