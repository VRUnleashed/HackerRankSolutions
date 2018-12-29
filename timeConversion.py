
def time_conversion(string):

    if string[0] == '1' and string[1] == '2':
        if 'AM' in string:
            s2 = string.split(':')
            s2[0] = '00'
            s3 = ':'.join(s2)
            s4 = s3.split('A')
            return s4[0]

        elif 'PM' in string:
            s5 = string.split('P')
            return s5[0]
    else:
        if 'AM' in string:
            s6 = string.split('A')
            return s6[0]
        elif 'PM' in string:
            s7 = string.split('P')
            s8 = s7[0]
            s9 = s8.split(':')
            h1 = int(s9[0])
            h2 = h1 + 12
            s9[0] = str(h2)
            return ':'.join(s9)


if __name__ == '__main__':
    s = '01:05:45PM'
    result = time_conversion(s)
    print(result)
