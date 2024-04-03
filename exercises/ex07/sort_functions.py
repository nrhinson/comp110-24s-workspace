"""Functions that implement sorting algorithms."""

__author__ = ""


def insertion_sort(x: list[int]) -> None:
    current_index: int = 1
    location_of_num_to_insert: int = 0
    for num_to_insert in x[1:]:
        location_of_num_to_insert = current_index
        for number in range(current_index):
            if (x[location_of_num_to_insert-1] > num_to_insert):
                x[location_of_num_to_insert] = x[location_of_num_to_insert-1] 
                x[location_of_num_to_insert-1] = num_to_insert
                location_of_num_to_insert -= 1
        current_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    index_of_current: int = 0
    current_min: int = 0
    index_of_min: int = 0
    stored_index: int = 0
    for selcted_number in x:
        current_min = selcted_number
        index_of_min = index_of_current
        stored_index = index_of_current
        for check_min in x[index_of_current:]:
            if current_min > check_min:
                current_min = check_min
                stored_index = index_of_min
            index_of_min += 1
        x[index_of_current] = current_min
        x[stored_index] = selcted_number
        index_of_current += 1
    return None
