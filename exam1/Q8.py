def print_pairs(lst, k):

    left, right = 0, 1

    while right < len(lst):
        if lst[right] - lst[left] == k:
            print(f"Pair Found: ({lst[left]}, {lst[right]})")
            right += 1
        elif lst[right] - lst[left] < k:
            right += 1
        else:
            left += 1

print_pairs([-7,-3,0,1,3,5,12,14,17,19,25,30], 6)
