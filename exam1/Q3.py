def exist(list, num):
    if not list:
        return False
    if list[0] == num:
        return True
    return exist(list[1:], num)

list = [1, 2, 3, 4, 5, 6]

print(exist(list,9))