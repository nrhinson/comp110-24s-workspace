"""EX05 - Dictionary Utils."""

__author__ = "730664337"

from exercises.ex05.dictionary import *
import pytest

def test_invert_use1 () -> None:
    """This tests the invert function once."""
    new_dict: dict[str, str] = {"key": "one", "anotherKey": "two"}
    changed_dict: dict[str, str] = invert(new_dict)
    assert changed_dict == {"one": "key", "two": "anotherKey"}


def test_invert_use2 () -> None:
    """this tests to make sure inverting the function twice returns it to its orignal value."""
    new_dict: dict[str, str] = {"key": "one", "anotherKey": "two"}
    changed_dict: dict[str, str] = invert(new_dict)
    changed_again_dict: dict[str, str] = invert(changed_dict)
    assert changed_again_dict == {"key": "one", "anotherKey": "two"}


def test_invert_edge () -> None:
    """This tests what happens when a int is used instead of a str."""
    new_dict: dict[str, int] = {"key": 1, "anotherKey": 2}
    changed_dict: dict[int, str] = invert(new_dict)
    assert changed_dict == {1: "key", 2: "anotherKey"}


def test_favorite_color_use1 () -> None:
    """This checks to make sure the most common color us pulled from the dictonary."""
    new_dict: dict[str, str] = {"Nick": "Green", "Joe": "Yellow", "Jackson": "Green", "Josh": "Blue"}
    new_str: str = favorite_color(new_dict)
    assert new_str == "Green"


def test_favorite_color_use2 () -> None:
    """This checks what happens if there is only one of each color."""
    new_dict: dict[str, str] = {"Nick": "Green", "Joe": "Yellow", "Jackson": "Orange", "Josh": "Blue"}
    new_str: str = favorite_color(new_dict)
    assert new_str == "Green"


def test_favorite_color_edge () -> None:
    """This checks what happens if the dictionary does not contain colors."""
    new_dict: dict[str, str] = {"Nick": "Apple", "Joe": "Watermelon", "Jackson": "Grapes", "Josh": "Oranges"}
    new_str: str = favorite_color(new_dict)
    assert new_str == "Apple"


def test_count_use1 () -> None:
    """This checks what happens when the def "count" is used as intended"""
    new_list: list[str] = ["Hi", "Hello", "Hi", "Hi", "Hello", "Hey"]
    new_dict: dict[str,str] = count(new_list)
    assert new_dict == {"Hi": 3, "Hello": 2, "Hey": 1}
    

def test_count_use2 () -> None:
    """This checks what happens when the list given is all one word"""
    new_list: list[str] = ["Hey", "Hey", "Hey", "Hey", "Hey", "Hey", "Hey"]
    new_dict: dict[str,str] = count(new_list)
    assert new_dict == {"Hey": 7}


def test_count_edge () -> None:
    """This checks what happens when an empty list is given"""
    new_list: list[str] = []
    new_dict: dict[str,str] = count(new_list)
    assert new_dict == {}


def test_alphabetizer_use1 () -> None:
    """This tests what happens when words are givin"""
    new_list: list[str] = ["Cat", "Dog", "Parrot", "Snake", "Turtle"]
    new_dict: dict[str, list[str]] = alphabetizer(new_list)
    assert new_dict == {"c": ["Cat"], "d": ["Dog"], "p": ["Parrot"], "s": ["Snake"], "t": ["Turtle"]}


def test_alphabetizer_use2 () -> None:
    """This tests what happens when a mix of lowercase and captial words are given"""
    new_list: list[str] = ["cat", "Dog", "parrot", "Snake", "Turtle"]
    new_dict: dict[str, list[str]] = alphabetizer(new_list)
    assert new_dict == {"c": ["cat"], "d": ["Dog"], "p": ["parrot"], "s": ["Snake"], "t": ["Turtle"]}


def test_alphabetizer_edge () -> None:
    """This tests what happens when numbers are given"""
    new_list: list[str] = ["1 cat", "2 Dog", "3 Parrot", "4 Snake", "5 Turtle"]
    new_dict: dict[str, list[str]] = alphabetizer(new_list)
    assert new_dict == {"1": ["1 cat"], "2": ["2 Dog"], "3": ["3 Parrot"], "4": ["4 Snake"], "5": ["5 Turtle"]}

    
def update_attendance_use1 () -> None:
    """This tests adding a student to an already existing day"""
    new_list: dict[str, list[str]] = {"Monday": ["Joe", "Jackson", "Nick"], "Tuesday": ["Nick", "Joe"], "Wendsay": ["Jackson", "Josh", "Alex"]}
    update_attendance(new_list, "Tuesday", "Alex")
    assert new_list == {"Monday": ["Joe", "Jackson", "Nick"], "Tuesday": ["Nick", "Joe", "Alex"], "Wendsay": ["Jackson", "Josh", "Alex"]}


def update_attendance_use2 () -> None:
    """This test adds a studnet to a day that does not exist"""
    new_list: dict[str, list[str]] = {"Monday": ["Joe", "Jackson", "Nick"], "Tuesday": ["Nick", "Joe"], "Wendsay": ["Jackson", "Josh", "Alex"]}
    update_attendance(new_list, "Tuesday", "Alex")
    assert new_list == {"Monday": ["Joe", "Jackson", "Nick"], "Wendsay": ["Jackson", "Josh", "Alex"]}
    

def update_attendance_edge () -> None:
    """This test test what happens when you add a name that already exists on said day"""
    new_list: dict[str, list[str]] = {"Monday": ["Joe", "Jackson", "Nick"], "Tuesday": ["Nick", "Joe", "Alex"], "Wendsay": ["Jackson", "Josh", "Alex"]}
    update_attendance(new_list, "Monday", "Joe")
    assert new_list == {"Monday": ["Joe", "Jackson", "Nick", "Joe"], "Tuesday": ["Nick", "Joe", "Alex"], "Wendsay": ["Jackson", "Josh", "Alex"]}