#!/usr/bin/python3
"""module to define lockboxes function"""


def canUnlockAll(boxes):
    """function to determine if all boxes can be opened"""
    unlocked = [boxes[0]]
    for box in unlocked:
        for key in box:
            if key < len(boxes) and boxes[key] not in unlocked:
                unlocked.append(boxes[key])

    return len(unlocked) == len(boxes)
