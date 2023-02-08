from typing import List

def list_sum(mylist: List[float]) -> float:
    s: float = 0.0
    for x in mylist:
        s += x
    return s

mylist = [1.0, 5.2, 7.9]