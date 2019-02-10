def birthday(s_local, d_local, m_local):

    n = len(s_local)
    sum_s = 0
    ways = 0

    for x in range(n):

        if m_local == 1:
            if s_local[x] == d_local:
                ways = ways + 1
        else:
            sum_s = 0

            for i in range(x, m_local + x):
                if (m_local + x) - 1 < n:
                    sum_s = sum_s + s_local[i]
                else:
                    break

            if sum_s == d:
                ways = ways + 1

    return ways


if __name__ == '__main__':

    s = [4]
    d = 4
    m = 1

    result = birthday(s, d, m)

    print(result)
