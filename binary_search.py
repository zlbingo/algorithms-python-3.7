"""
函数说明:二分查找

Parameters:
    lst - 有序列表
    item - 要查找的数

Returns:
     要查找的数在列表中的位置
"""


def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while low <= high:

        mid = (low+high)//2

        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        # 停止条件：1. guess == item
        # 停止条件：2.当item<lst[0]时  low>high break
        # 停止条件：3.当item>lst[-1]时  high<low break
    return None


a = [1, 3, 6, 9, 11, 56, 89]
print(binary_search(a, 11))


