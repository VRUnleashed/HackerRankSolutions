def birthdayCakeCandles(ar):

    max = ar[0]
    flag = 0

    for x in range(len(ar) - 1):
        if max >= ar[x + 1]:
            pass
        elif max < ar[x + 1]:
            max = ar[x + 1]

    for x in range(len(ar)):
        if max == ar[x]:
            flag = flag + 1
        else:
            pass

    print(flag)

ar = [1, 3, 2, 4]

birthdayCakeCandles(ar)
