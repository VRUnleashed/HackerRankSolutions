def grading_students(grades_local):

    grades_cpy = grades_local

    l = len(grades_cpy)

    for i in range(0, l):
        if grades_cpy[i] < 38:
            pass
        elif grades_cpy[i] % 5 == 0:
            pass
        else:
            for x in range(40, 105, 5):
                if grades_cpy[i] < x:
                    if x - grades_cpy[i] < 3:
                        grades_cpy[i] = x

    return grades_cpy


if __name__ == '__main__':
    grades = [73, 67, 38, 98]

    result = grading_students(grades)

    print(result)
