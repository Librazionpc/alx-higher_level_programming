#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as result:
        print("Body response:")
        print("\t- type:", type(result.read()))
        print("\t- content:", result.read())
        print("\t- utf8 content:", result.read().decode('utf-8'))
