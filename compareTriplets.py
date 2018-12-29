def compare_triplets(a, b):
    s = int(0)
    t = int(0)

    for i in range(0, 3):
        if a[i] > b[i]:
            s = s + 1
        elif b[i] > a[i]:
            t = t + 1

    r = s, t

    return r


if __name__ == '__main__':
    result = compare_triplets([1, 2, 5], [0, 7, 3])
    print(result)
