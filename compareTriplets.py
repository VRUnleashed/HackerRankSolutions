def compareTriplets(a, b):
    r = []
    s = int(0)
    t = int(0)

    for i in range(0, 3):
        if a[i] > b[i]:
            s = s + 1
        elif b[i] > a[i]:
            t = t + 1

    #r.append(s)
    #r.append(t)

    r = s, t

    return r

result = compareTriplets([1, 2, 5], [0, 7, 3])

print(result)
