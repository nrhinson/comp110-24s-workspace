"""Test my garden functions."""

from garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


#Define dicts being used. 

def test_add_by_kind_use() -> None:
    """This def tests a use case for the test_add_by_kind function from garden helpers"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots", "green beans"], "fruit": ["apple", "blueberry"]}
    add_by_kind(by_kind, "flower", "lily")
    assert "lily" in by_kind["flower"]

def test_add_by_kind_edge() -> None:
    """This def tests an edge case for the test_add_by_kind function from garden helpers"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots", "green beans"], "fruit": ["apple", "blueberry"]}
    add_by_kind(by_kind, 12, 4)
    assert 4 not in by_kind

def test_add_by_date_use() -> None:
    """"This def tests a use case of the add_by_date function from garden helpers"""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "May": ["rose"], "November": ["marigold", "green beans"], "December":["lily"]}
    add_by_date(by_date, "June", "rose")
    assert "rose" in by_date["June"]


def test_add_by_date_edge() -> None:
    """"This def tests a edge case of the add_by_date function from garden helpers"""
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "May": ["rose"], "November": ["marigold", "green beans"], "December":["lily"]}
    add_by_date(by_date, "flower", "lily")
    assert "lily" in by_date["flower"]


def test_lookup_by_kind_and_date_use() -> None:
    """This def tests a use case of the lookup_by_kind_and_date function from garden helpers"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots", "green beans"], "fruit": ["apple", "blueberry"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "May": ["rose"], "November": ["marigold", "green beans"], "December":["lily"]}
    t: str = lookup_by_kind_and_date(by_kind, by_date, "flower", "May")
    assert t == "flowers to plant in May: ['rose']"

def test_lookup_by_kind_and_date_edge() -> None:
    """This def tests a edge case of the lookup_by_kind_and_date function from garden helpers"""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots", "green beans"], "fruit": ["apple", "blueberry"]}
    by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "May": ["rose"], "November": ["marigold", "green beans"], "December":["lily"]}
    t: str = lookup_by_kind_and_date(by_kind, by_date, "Not a real plant", "Not a real month")
    assert t == "No Not a real plants to plant in Not a real month"