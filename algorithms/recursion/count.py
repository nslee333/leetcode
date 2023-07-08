# Recursive function that counts how many elements in the list.
# `python3 count_items.py` to run 


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1,2,3,4,5]))