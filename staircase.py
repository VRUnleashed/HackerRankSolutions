def staircase(n):

    for x in range(1, n + 1):
        stair = "{}{}"
        print(stair.format(' ' * int(n - x), '#' * int(x)))

staircase(10)
