"""Summing the elements of a list using different loops."""

__author__ = "730664337"


def w_sum(vals: list[float]) -> float:
    """This function uses a while loop to add all floats in a list."""
    total: float = 0.0
    listIndex: int = 0
    while listIndex < len(vals):
        total += vals[listIndex]
        listIndex += 1
    return total


def f_sum(vals: list[float]) -> float:
    """This function uses a for loop to add all floats in a list."""
    total: float = 0.0
    for index in vals:
        total += index
    return total


def f_range_sum(vals: list[float]) -> float:
    """This function uses a for - in - range loop to add all floats in a list."""
    total: float = 0.0
    for index in range(0, len(vals)):
        total += vals[index]
    return total