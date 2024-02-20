"""EX04"""

__author__ = "730664337"

def all(listA: list[int], givenInt: int) -> bool:
    """This function is meant to check to see if the give int is the only int in the list"""
    index: int = 0
    if len(listA) == 0:
        return False
    while index < len(listA):
        if givenInt != listA[index]:
            return False
        index += 1
    return True


def max(listB: list[int]) -> int:
    """This function is meant to find the largest number in a list"""
    index: int = 1
    highestNum: int = listB[0]
    while index < len(listB):
        if highestNum < listB[index]:
            highestNum = listB[index]
        index += 1
    return highestNum


def is_equal(listC: list[int], listD: list[int]) -> bool:
    """This function is meant to find if two lists are identical to each other"""
    index: int = 0
    if len(listC) != len(listD):
        return False
    while index < len(listC):
        if listC[index] != listD[index]:
            return False
    return True


def extend(baseList: list[int], addList: list[int]) -> None:
    """This functions is meant to add a list to another list"""
    index: int = 0
    while index < len(addList):
        baseList.append(addList[index])
        index += 1