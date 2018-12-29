def kangaroo(x1, v1, x2, v2):
    flag = 0

    if x2 > x1 and v2 > v1:
        return "NO"
    elif x1 > x2 and v1 > v2:
        return "NO"
    else:

        for i in range(0, 10000):
            x1 = x1 + v1
            x2 = x2 + v2

            if x1 == x2:
                flag = 1
                break
            else:
                flag = 0

        if flag == 1:
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    result = kangaroo(0, 2, 5, 3)
    print(result)
