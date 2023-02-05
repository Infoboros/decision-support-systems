def equal_list(arr1, arr2) -> bool:
    if (type(arr1) is not list) and (type(arr2) is not list):
        return arr1 == arr2

    for arr1_item, arr2_item in zip(arr1, arr2):
        return equal_list(arr1_item, arr2_item)