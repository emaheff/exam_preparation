import sys


def max_mul2(lst):
    max1 = max(lst)
    max2 = -sys.maxsize
    min1 = min(lst)
    min2 = sys.maxsize
    for num in lst:
        if num > max2 and num != max1:
            max2 = num
        if num < min2 and num != min1:
            min2 = num
    return max(max1 * max2, min1 * min2)



