from typing import List


def convert_list_to_dict(lst: List[str]):
    result = {}
    for i in range(0, len(lst), 2):
        if i + 1 < len(lst):
            result[lst[i]] = lst[i + 1]
    return result
