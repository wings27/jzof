#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: zhaoyilei

'''
输入：
    输入可能包含多个测试样例。
    对于每个测试案例，输入的第一行为一个整数m (1<=m <=100)代表输入的正整数的个数。
    输入的第二行包括m个正整数，其中每个正整数不超过10000000。
输出：
    对应每个测试案例，
    输出m个数字能排成的最小数字。
Input：
    3
    23 13 6
    2
    23456 56
Output：
    13236
    2345656
'''
import sys


def read():
    for line in sys.stdin:
        for s in line:
            yield s


def comparestr(str1, str2):
    string1 = str(str1) + str(str2)
    string2 = str(str2) + str(str1)
    if string1 <= string2:
        return string1
    else:
        return string2


def output_min_num(str_list):
    length = len(str_list)
    min_num = -1
    if length < 1:
        return min_num
    elif length == 1:
        return str_list[0]

    for i in range(length - 1):
        if (min_num > temp) or (min_num < 0):
            min_num = temp
    return min_num


def comp(a, b, comparing_func=lambda x, y: x < y):
    if comparing_func(a, b):
        return a
    else:
        return b


def quick_sort(arr, left, right, compare_function=lambda x, y: x < y):
    if left == right:
        return
    pivot = arr[left]
    i = left
    j = right
    while i <= j:
        while arr[i] <= pivot:
            i+=1
        while arr[j] >= pivot:
            j+=1
            
        

def main():
    rev_comp = lambda x, y: x > y
    print(comp(3, 5, rev_comp))


if __name__ == '__main__':
    main()
