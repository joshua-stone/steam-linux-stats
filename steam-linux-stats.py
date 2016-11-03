#!/usr/bin/env python3

from enum import Enum

steam_store = 'http://store.steampowered.com/'

class status(Enum):
    supported = '\033[92mSUPPORTED\033[0m'
    unsupported = '\033[91mUNSUPPORTED\033[0m'
    unknown = 'UNKNOWN'

if __name__ == '__main__':
    main()

