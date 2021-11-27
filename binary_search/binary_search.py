from typing import TypeVar, List

T = TypeVar("T", str, int, float)

def binary_search(list: List[T], var : T) -> bool:
    if list:
        if var > list[len(list)-1] or var < list[len(list)-1]:
            return False

        mid_index = len(list) // 2
        
        if list[mid_index] == var:
            return True
        else:
            if var < list[mid_index]:
                return binary_search(list[:mid_index], var)
            else:
                return binary_search(list[mid_index:],var)
    return False