"""EX05 - Dictionary Utils."""

__author__ = "730664337"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and indexs of a dictionary."""
    return_dict: dict[str, str] = {}
    for i in given_dict:
        return_dict[given_dict[i]] = i
    return return_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """This function counts the most common colors out of a list of people and their favorte color."""
    most_common_color: str
    most_common_colorCount: int = 0
    counter: int
    for i in given_dict:
        counter = 0
        for b in given_dict:
            if given_dict[i] == given_dict[b]:
                counter += 1
        if counter > most_common_colorCount:
            most_common_color = given_dict[i]
            most_common_colorCount = counter
    return most_common_color


def count(givenList: list[str]) -> dict[str, int]:
    """This function counts how much of each string is in a list."""
    how_much: int = 0
    return_dict: dict[str, int] = {}
    for a in givenList:
        already_ran: bool = False
        for b in return_dict:
            if b == a:
                already_ran = True
        if not already_ran:
            how_much = 0
            for c in givenList:
                if c == a:
                    how_much += 1
            return_dict[a] = how_much
    return return_dict


def alphabetizer(givenList: list[str]) -> dict[str, list[str]]:
    """This function sorts words in a list by the first letter of their string."""
    return_dict: dict[str, list[str]] = {}
    build_list: list[str] = []
    for a in givenList:
        a = a[0].lower()
        build_list = []
        already_ran: bool = False
        for b in return_dict:
            b = b[0].lower()
            if a == b:
                already_ran = True
        if not already_ran:
            for c in givenList:
                if c[0].lower() == a:
                    build_list.append(c)
            return_dict[a] = build_list
    return return_dict


def update_attendance(given_dict: dict[str, list[str]], day: str, student: str) -> None:
    """This function is used to update attendance."""
    key_already_used: bool = False
    new_list: list[str]
    for i in given_dict:
        if day == i:
            key_already_used = True
    if key_already_used:
        new_list = given_dict[day]
        new_list.append(student)
        given_dict[day] = new_list
    else:
        given_dict[day] = [student]