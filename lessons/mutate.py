"""Mutating functions."""

__author__ = "730664337"


def manual_append(int_list: list[int], new_int: int) -> None:
    """This fnction adds number to list."""
    int_list.append(new_int)


def double(int_list: list[int]) -> None:
    """This function doubles list."""
    listLength: int = len(int_list) - 1
    count: int = 0
    while (count <= listLength):
        int_list[count] = int_list[count] * 2
        count = count + 1
    
