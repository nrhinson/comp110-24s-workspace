"""Splitting a dictionary into two lists."""

__author__ = "730664337"


def get_keys (givenDict: dict[str, int]) -> list:
    """This function returns all the keys in a dictonary."""
    returnList: list = []
    for i in givenDict:
        returnList.append(i)
    return returnList


def get_values (givenDict: dict[str, int]) -> list:
    """This function returns all the values in a dictonary."""
    returnList: list = []
    for i in givenDict:
        returnList.append(givenDict[i])
    return returnList