# -*- coding: utf-8 -*-

import json

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen


def get_chuck_nerd_jokes():
    url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'
    response = urlopen(url).readall().decode('utf-8')
    data = json.loads(response)
    d = data['value']
    return d['joke']


if __name__ == '__main__':
    print(get_chuck_nerd_jokes())
