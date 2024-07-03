def printQuestion(Q):
    print('')

    seperator = ['**' for char in Q]
    seperator = ''.join(seperator)

    print(seperator.center(100))
    print(Q.center(100))
    print(seperator.center(100))

    print('')


def intList(list):
    seq_ = []
    for num in list:
        seq_.append(int(num))
    return seq_
