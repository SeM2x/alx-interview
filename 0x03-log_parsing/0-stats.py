#!/usr/bin/python3
"""
This script parses log lines from standard input,
extracts relevant information, and prints statistics every 10 lines.
"""
import sys


def parse_line(line: str):
    """
    Parses a log line and returns a dictionary with IP, date, request, status,
    and size if valid, otherwise returns False.
    """
    if not line or len(line) == 0:
        return False
    ip = line.split("-")[0]
    if len(ip) == 0:
        return False
    date = line[line.find("[") + 1: line.find("]")]
    if len(date) == 0:
        return False
    req = line[line.find('"') + 1: line.find('"', line.find('"') + 1)]
    if req != "GET /projects/260 HTTP/1.1":
        return False
    status = line.split(" ")[-2]
    try:
        if int(status) not in [200, 301, 400, 401, 403, 404, 405, 500]:
            return False
    except Exception:
        return False

    size = line.split(" ")[-1][:-1]
    try:
        int(size)
    except Exception:
        return False

    return {"ip": ip, "date": date, "request":
            req, "status": status, "size": int(size)}


def get_stats(lines: list[str]):
    """
    Calculate and print the total file size and the count
    of each HTTP status code from a list of log lines.
    """
    file_size = 0
    status_count = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    for line in lines:
        file_size += parse_line(line)["size"]
        status_count[parse_line(line)["status"]] += 1

    print(f"File size: {file_size}")
    for key, val in status_count.items():
        if val > 0:
            print(f"{key}: ", val)


count = 0
lines = []
try:
    for line in sys.stdin:
        if parse_line(line) is not False:
            lines.append(line)
            count += 1
            if count % 10 == 0:
                get_stats(lines)
except KeyboardInterrupt:
    get_stats(lines)
