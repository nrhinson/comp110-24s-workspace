"""Some functions for my garden plan!"""

__author__ = "730664337"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """This function adds a plant based on kind"""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """This function adds a plant based on date"""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """This function looks up a plant based on date and type and returns a string accordingly"""
    if (plant_kind in plants_by_kind) and (month in plants_by_date):
        list_of_plants_by_kind: list[str] = plants_by_kind[plant_kind]
        list_of_plants_by_date: list[str] = plants_by_date[month]
        return_list_of_plants: list[str] = []
        list_used_check: bool = False
        for a in list_of_plants_by_kind:
            for b in list_of_plants_by_date:
                if a == b:
                    return_list_of_plants.append(a)
                    list_used_check = True
        if list_used_check:
            return (f"flowers to plant in {month}: " + str(return_list_of_plants))
        else:
            return f"No {plant_kind}s to plant in {month}"
    else:
        return f"No {plant_kind}s to plant in {month}"