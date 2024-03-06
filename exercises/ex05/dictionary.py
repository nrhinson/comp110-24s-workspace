"""EX05 - Dictionary Utils."""

__author__ = "730664337"


def invert(givenDict: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and indexs of a dictionary."""
    returnDict: dict[str, str] = {}
    for i in givenDict:
        returnDict[givenDict[i]] = i
    return returnDict


def favorite_color(givenDict: dict[str, str]) -> str:
    """This function counts the most common colors out of a list of people and their favorte color."""
    mostCommonColor: str
    mostCommonColorCount: int = 0
    counter: int
    for i in givenDict:
        counter = 0
        for b in givenDict:
            if givenDict[i] == givenDict[b]:
                counter += 1
        if counter > mostCommonColorCount:
            mostCommonColor = givenDict[i]
            mostCommonColorCount = counter
    return mostCommonColor


def count(givenList: list[str]) -> dict[str, int]:
    """This function counts how much of each string is in a list."""
    howMuch: int = 0
    returnDict: dict[str, int] = {}
    for a in givenList:
        alreadyRan: bool = False
        for b in returnDict:
            if b == a:
                alreadyRan = True
        if not alreadyRan:
            howMuch = 0
            for c in givenList:
                if c == a:
                    howMuch += 1
            returnDict[a] = howMuch
    return returnDict


def alphabetizer(givenList: list[str]) -> dict[str, list[str]]:
    """This function sorts words in a list by the first letter of their string."""
    returnDict: dict[str, list[str]] = {}
    buildList: list[str] = []
    for a in givenList:
        a = a[0].lower()
        buildList = []
        alreadyRan: bool = False
        for b in returnDict:
            b = b[0].lower()
            if a == b:
                alreadyRan = True
        if not alreadyRan:
            for c in givenList:
                if c[0].lower() == a:
                    buildList.append(c)
            returnDict[a] = buildList
    return returnDict


def update_attendance(givenDict: dict[str, list[str]], day: str, student: str) -> None:
    """This function is used to update attendance."""
    keyAlreadyUsed: bool = False
    newList: list[str]
    for i in givenDict:
        if day == i:
            keyAlreadyUsed = True
    if keyAlreadyUsed:
        newList = givenDict[day]
        newList.append(student)
        givenDict[day] = newList
    else:
        givenDict[day] = [student]