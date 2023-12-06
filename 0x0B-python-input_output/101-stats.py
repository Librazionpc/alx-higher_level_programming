#!/usr/bin/python3
"""More advance"""
import sys


def print_stats(ttl_size, stat_code):
    """prints stat func"""
    print(f"File size: {ttl_size}")
    for code in sorted(stat_code.keys()):
        if stat_code[code] > 0:
            print(f"{code}: {stat_code[code]}")


lines = 0
ttl_size = 0
stat_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        lines += 1
        parts = line.split()
        if len(parts) > 2:
            try:
                size = int(parts[-1])
                code = int(parts[-2])
                ttl_size += size
                if code in stat_code:
                    stat_code[code] += 1
            except ValueError:
                pass

        if lines % 10 == 0:
            print_stats(ttl_size, stat_code)

except KeyboardInterrupt:
    print_stats(ttl_size, stat_code)
