def breaking_records(scores_local):

    num = len(scores_local)
    min_s = scores_local[0]
    max_s = scores_local[0]
    min_count = 0
    max_count = 0

    for x in range(num):

        if scores_local[x] < min_s:
            min_s = scores_local[x]
            min_count = min_count + 1
        elif scores_local[x] > max_s:
            max_s = scores_local[x]
            max_count = max_count + 1

    print(f"{max_count} {min_count}")


if __name__ == '__main__':

    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

    breaking_records(scores)
