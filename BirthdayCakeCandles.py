
def birthday_cake_candles(array):

    maximum = array[0]
    flag = 0

    for x in range(len(array) - 1):
        if maximum >= array[x + 1]:
            pass
        elif maximum < array[x + 1]:
            maximum = array[x + 1]

    for x in range(len(array)):
        if maximum == array[x]:
            flag = flag + 1
        else:
            pass

    print(flag)


if __name__ == '__main__':
    ar = [1, 3, 2, 4]
    birthday_cake_candles(ar)
