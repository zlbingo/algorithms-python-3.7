"""
函数说明:选择排序

Parameters:
    arr - 随机数组


Returns:
     从小到大排序的数组
"""

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
        # pop每次从arr弹出smallest这个位置的元素
        # 若想从大到小排序，可使用
        # newarr.reverse()
        # 或使用
        # newarr.sort(reverse=True)
        # reverse -- 排序规则，reverse = True 降序，
        # reverse = False 升序（默认）
    return newarr


print(selectsort([5, 3, 6, 2, 10]))
