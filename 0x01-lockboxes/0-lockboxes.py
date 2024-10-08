#!/usr/bin/python3
"""module to define lockboxes function"""


def canUnlockAll(boxes):
    """function to determine if all boxes can be opened"""
    if not boxes:
        return False

    unlocked = [boxes[0]]
    keys = [0]
    for box in unlocked:
        for key in box:
            if key < len(boxes) and key not in keys:
                unlocked.append(boxes[key])
                keys.append(key)

    return len(unlocked) == len(boxes)
