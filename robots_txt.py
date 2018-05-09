'''
	Use requests to get the robots.txt
'''

import os
import requests

def get_robots_txt(url):
    # Check for a forward-slash
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    r = requests.get(path + 'robots.txt')
    return r.text
