#!/usr/bin/env python3

from enum import Enum

steam_store = 'http://store.steampowered.com/'

class status(Enum):
    supported = '\033[92mSUPPORTED\033[0m'
    unsupported = '\033[91mUNSUPPORTED\033[0m'
    unknown = 'UNKNOWN'

def is_supported(store_url):
    if store_url.startswith('{}app/'.format(steam_store)):
        store_id = store_url.split('/')[-2]
        api_url = '{}api/appdetails?appids={}'.format(steam_store, store_id)

        json = loads(urlopen(api_url).read().decode())
        linux_support = json[store_id]['data']['platforms']['linux']

        if linux_support:
            support_status = status.supported
        else:
            support_status = status.unsupported
    else:
        support_status = status.unknown

    return support_status


if __name__ == '__main__':
    main()

