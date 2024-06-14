def bulls_and_cows(number, guess):
    res = 0
    check_list = [True for _ in range(len(number))]
    for i in range(len(number)):
        for j in range(len(guess)):
            if number[i] == guess[j] and check_list[i]:
                if i == j:
                    res += 2
                else:
                    res += 1
                check_list[i] = False

    return res

