#!/usr/bin/env python3
import calendar
import logging
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.WARN,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_latest_artifacts(user, password, url, **kwargs):
    count = 0
    limit = kwargs.get('limit', -1)
    d = defaultdict(list)
    latest_artifacts = []

    data = requests.get(url, auth=(user, password)).text
    soup = BeautifulSoup(data, 'html.parser')

    logging.debug('')
    logging.debug(url)
    logging.debug('')
    logging.debug(data)

    for link in soup.find_all('a'):
        fileName = link.get('href')
        if '../' != fileName:
            lastModified = link.nextSibling.strip()[:-1].strip()
            date, time = lastModified.split(' ')
            hour, minute = time.split(':')
            day, month_abbr, year = date.split('-')
            month = '{0:02d}'.format(list(calendar.month_abbr).index(month_abbr))

            TIME = hour + '.' + minute
            DATE = year + '-' + month + '-' + day

            key = DATE + '.' + TIME
            value = fileName

            d[key].append(value)

    for k in sorted(d, reverse=True):
        for f in d[k]:
            if count == limit:
                break
            logging.info(k + ' ' + f)
            latest_artifacts.append(f)
            count += 1

    return latest_artifacts

if __name__ == '__main__':
    USER = 'ray'
    PASS = 'wong'
    PATH = ''
    ARTIFACT = 'test'

    SERVER = 'http://localhost:8080/'
    URL = SERVER + PATH + ARTIFACT + '/'

    print(get_latest_artifacts(user=USER, password=PASS, url=URL))
    print(get_latest_artifacts(user=USER, password=PASS, url=URL, limit=2))
