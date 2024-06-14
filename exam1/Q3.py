def exist(list, num):
    if not list:
        return False
    if list[0] == num:
        return True
    return exist(list[1:], num)


def find_pair(sum, lst):
    for i in range(len(lst)):
        #  creating new list without the current item in the list
        new_list = [item for item in lst if item != lst[i]]
        if exist(new_list, sum - lst[i]):
            return True
    return False


list = [1, 2, 3, 4, 5, 6]

print(find_pair(11, list))
