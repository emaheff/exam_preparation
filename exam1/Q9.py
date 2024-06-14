def maximal_drop(lst):
    if not lst:
        return 0  # If the list is empty, return 0

    max_drop = 0
    peak = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > peak:
            peak = lst[i]
        else:
            drop = peak - lst[i]
            if drop > max_drop:
                max_drop = drop

    return max_drop

print(maximal_drop([14,26,7,12,22,3,21,5]))