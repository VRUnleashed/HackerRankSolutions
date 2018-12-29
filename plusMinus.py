def plus_minus(arr):

    n = 0
    p = 0
    z = 0

    for x in arr:

        if x < 0:
            n = n + 1
        elif x > 0:
            p = p + 1
        elif x == 0:
            z = z + 1

    l = len(arr)

    print(round(p/l, 6))
    print(round(n/l, 6))
    print(round(z/l, 6))


def main():
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr)


if __name__ == '__main__':
    main()
