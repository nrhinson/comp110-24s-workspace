"""Functions that implement sorting algorithms."""

__author__ = ""


def insertion_sort(x: list[int]) -> None:
    stored_int: int = 0
    num_of_sorted_int: int = 0
    for index in x:
        currentInt: int = index
        for potental_greater in x:
            print("2")
            if currentInt > second_index:  
                print("3")
                stored_int = x[index]
                x[index] = currentInt
                x[second_index] = stored_int
                currentInt = x[index]
        num_of_sorted_int =+ 1
    return None


def selection_sort(x: list[int]) -> None:
    index_of_current: int = 0
    current_min: int = 0
    index_of_min: int = 0
    stored_index: int = 0
    swap_number: int = 0
    for selcted_index in x:
        current_min = selcted_index
        index_of_min = index_of_current
        for check_min in x[index_of_current:]:
            if current_min > check_min:
                current_min = check_min
                stored_index = index_of_min
            index_of_min += 1
        swap_number = x[stored_index]
        x[stored_index] = x[index_of_current]
        x[index_of_current] = swap_number
        index_of_current += 1
    return None

list1: list[int] = [2, 4, 3, 6]
selection_sort(list1)
print(list1)