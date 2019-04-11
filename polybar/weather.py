#!/usr/bin/env python3

import json
import urllib
import urllib.parse
import urllib.request
import os


def main():
    try:
        degree_sign = u'\u00b0'
        with open(os.path.join(
                os.path.expanduser("~"),
                '.config',
                'polybar',
                'city')) as f:
            city = f.readline().strip()
        with open(os.path.join(
                os.path.expanduser("~"),
                '.config',
                'polybar',
                'weather.json')) as f:
            api_key = json.load(f)['api_key']
    except Exception as e:
        print(e)
        #return '-'

    try:
        data = urllib.parse.urlencode({'q': city, 'appid': api_key})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        temp = int(float(weather['main']['temp']) - 272.15)
        return ('{}, {}'+degree_sign+'C').format(desc, temp)
    except Exception as e:
        print(e)
        #return'-'


if __name__ == "__main__":
    print(main())
