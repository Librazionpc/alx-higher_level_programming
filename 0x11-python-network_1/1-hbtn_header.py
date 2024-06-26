#!/usr/bin/python3
"""Python script that takes URL, sends a request to the URL and then displays
   the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as result:
        html = result.info()
        value = html.get('X-Request-Id')
        print(value)
