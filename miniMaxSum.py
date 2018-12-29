def min_max_sum(arr_local):
    min_local = 0
    max_local = 0
    a = arr_local[0]
    b = arr_local[0]

    for x in range(4):
        if a <= arr_local[x + 1]:
            pass
        elif a > arr_local[x + 1]:
            a = arr_local[x + 1]

    for x in range(4):
        if b >= arr_local[x + 1]:
            pass
        elif b < arr_local[x + 1]:
            b = arr_local[x + 1]

    for x in range(5):
        max_local = max_local + arr_local[x]
        min_local = min_local + arr_local[x]

    max_local = max_local - a
    min_local = min_local - b

    print(min_local, max_local)


if __name__ == '__main__':
    arr = [3, 1, 4, 5, 5]
    min_max_sum(arr)
