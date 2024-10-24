#!/usr/bin/python3
"""A script for parsing HTTP request logs.
"""


def get_stats(lines: list[str]):
    """Print the total file size and status count"""
    file_size = 0
    status_count = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0,
    }
    for line in lines:
        size = int(line.split(" ")[-1][:-1])
        status = line.split(" ")[-2]
        file_size += size
        status_count[status] += 1

    print(f"File size: {file_size}")
    for key, val in status_count.items():
        if val > 0:
            print(f"{key}: ", val)


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
