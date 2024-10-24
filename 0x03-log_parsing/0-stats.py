#!/usr/bin/python3
"""A script for parsing HTTP request logs.
"""


if __name__ == '__main__':
    count = 0
    lines = []
    try:
        while True:
            lines.append(input())
            count += 1
            if count % 10 == 0:
                get_stats(lines)
    except (KeyboardInterrupt, EOFError):
        get_stats(lines)
