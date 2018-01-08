#!/usr/bin/env python
from deviceidentifier import api

import sys, json


def main():
    # Sample showing how to identify an unknown identifier.

    if len(sys.argv) < 2:
        print 'Usage: provide an unknown identifier for a list of potential identities.'
        exit(-1)

    print json.dumps(
        api.identify_identifier( sys.argv[1:][0] ),
        indent=4, sort_keys=True, ensure_ascii=False, encoding='utf8'
    )

if __name__ == '__main__':
    main()
