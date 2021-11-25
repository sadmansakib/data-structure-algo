from typing import List, TypeVar

T = TypeVar("T")

def linear_search(list: List[T], val: T) -> int:
    if list:
        if list[0] == val:
            return 0
        elif list[len(list)-1] == val:
            return len(list)-1
        else:
            for index, v in enumerate(list):
                if v == val:
                    return index
    return -1