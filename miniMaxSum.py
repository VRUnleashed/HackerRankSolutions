def miniMaxSum(arr):
    min = 0
    max = 0
    a = arr[0]
    b = arr[0]

    for x in range(4):
        if a <= arr[x + 1]:
            pass
        elif a > arr[x + 1]:
            a = arr[x + 1]

    for x in range(4):
        if b >= arr[x + 1]:
            pass
        elif b < arr[x + 1]:
            b = arr[x + 1]

    for x in range(5):
        max = max + arr[x]
        min = min + arr[x]

    max = max - a
    min = min - b

    print(min, max)

arr = [3, 1, 4, 5, 5]
miniMaxSum(arr)
