# -*- coding:utf-8 -*-
"""函数说明:冒泡排序（升序）
    Parameters:
        input_list - 待排序列表
    Returns:
        sorted_list - 升序排序好的列表
"""


def bubblesort(arr):
    if len(arr) == 0:
        return []
    sorted_list = arr
    for i in range(len(sorted_list)-1):
        print('第%d次排序' % (i+1))
        # n个数只需要排n-1个数即可
        # n-1个数排序过程中每次将剩余元素中最大的放在序列最后
        for j in range(len(sorted_list)-1):
            # range的取值是[0,len(input_list)-1),左开右闭
            # 当j取到列表倒数第二个索引结束，
            # 这时 sorted_list[j+1]刚好为列表的最后一个数
            if sorted_list[j+1] < sorted_list[j]:
                sorted_list[j+1], sorted_list[j] = sorted_list[j], sorted_list[j+1]
            print(sorted_list)
    return sorted_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print('排序前:', input_list)
    sorted_list = bubblesort(input_list)
    print('排序后:', sorted_list)



