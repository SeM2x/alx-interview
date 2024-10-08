#!/usr/bin/python3
"""module to define lockboxes function"""


def canUnlockAll(boxes):
    """Function to determine if all boxes can be opened"""
    if not boxes:
        return False
    unlocked = [0]
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key not in unlocked:
                unlocked.append(key)
                new_keys.update(boxes[key])
        keys = new_keys

    return len(unlocked) == len(boxes)
