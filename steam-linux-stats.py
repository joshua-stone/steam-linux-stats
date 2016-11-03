#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
from json import loads
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

def top_games():
    html = urlopen('{}stats/'.format(steam_store))
    bs = BeautifulSoup(html.read(), 'html.parser')
    top_games = bs.findAll('tr', class_='player_count_row')

    for game in [game.contents for game in top_games]:
        current, peak = game[1].contents[1].contents[0], game[3].contents[1].contents[0]
        title, store_url = game[7].contents[1].get_text(), game[7].contents[1].get('href')

        support_status = is_supported(store_url)

        yield (current, peak, title, support_status.value)

if __name__ == '__main__':
    main()

