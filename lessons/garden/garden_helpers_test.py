"""Test my garden functions."""

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

def test_add_by_kind() -> None:
    """This def tests the test_add_by_kind function from garden helpers"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots", "green beans"], "fruit": ["apple", "blueberry"]}

def test_add_by_date() -> None:
    """"This def tests the add_by_date function from garden helpers"""
    by_date: dict[str, list[str]]

def test_lookup_by_kind_and_date() -> None:
    """This def tests the lookup_by_kind_and_date function from garden helpers"""
    #Test 1 (use case).
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots", "green beans"], "fruit": ["apple", "blueberry"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "May": ["rose"], "November": ["marigold", "green beans"], "December":["lily"]}
    t: str = lookup_by_kind_and_date(by_kind, by_date, "May", "flower")
    assert t == "flowers to plant in May: ['rose']"
    #Test 2 (edge case)