def find_negation(lst, current, index):
    if index >= len(lst):
        return False
    if lst[index] == -current:
        return True
    return find_negation(lst, current, index + 1)


def helper(lst, index):
    if index >= len(lst):
        return True
    current = lst[index]
    if find_negation(lst, current, 0):
        return helper(lst, index + 1)
    return False


def minus_plus(lst):
    return helper(lst, 0)


lst = [2, -2, 5, -5, -7, 7, 3, -3]
print(minus_plus(lst))
