def get_total_x(a_local, b_local):

    n = len(a_local)

    a_last = a_local[n - 1]
    b_start = b_local[0]
    flag = 0
    count = 0

    for x in range(a_last, b_start + 1):

        for i in a_local:
            if x % i == 0:
                flag = 0
            elif x % i != 0:
                flag = 1
                break

        if flag == 0:
            for i in b_local:
                if i % x == 0:
                    flag = 0
                elif i % x != 0:
                    flag = 1
                    break

        if flag == 0:
            count = count + 1

    return count


if __name__ == '__main__':

    a = [3, 4]
    b = [24, 48]

    result = get_total_x(a, b)

    print(result)
