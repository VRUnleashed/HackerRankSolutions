def count_apples_and_oranges(s, t, a, b, apples, oranges):

    h = len(apples)
    k = len(oranges)
    y = 0
    z = 0

    for i in range(0, h):
        if (apples[i] + a) >= s and apples[i] + a <= t:
            y = y + 1

    for i in range(0, k):
        if (oranges[i] + b >= s) and oranges[i] + b <= t:
            z = z + 1

    print(y)
    print(z)


if __name__ == '__main__':
    count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])