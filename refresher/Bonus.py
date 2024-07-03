import utils

try:
    # Bonus Solution

    # Find the Longest Consecutive Sequence in a List of Integers:
    Q_ = 'Find the Longest Consecutive Sequence in a List of Integers'
    utils.printQuestion(Q_)

    integersList = input('Enter integers separated by space: ')
    integersList = integersList.split(' ')
    integersList = utils.intList(integersList)

    def findConsecutiveSeq_(ints_list):
        ints_list.sort(reverse=True)

        consecutive_ints = []

        for index, int_ in enumerate(ints_list, start=1):
            if 0 <= index < len(ints_list):
                if int_ - ints_list[index] == 1:
                    consecutive_ints.append(int_)

        last_consecutive_int = consecutive_ints[len(consecutive_ints)-1]
        last_ints_list_int = ints_list[len(ints_list)-1]

        if last_consecutive_int - last_ints_list_int == 1:
            consecutive_ints.append(last_ints_list_int)

        return consecutive_ints

    consecutive_seq = findConsecutiveSeq_(integersList)

    print(f'Longest consecutive sequence length: {len(consecutive_seq)}')

except Exception as error:
    print(error)
else:
    print('\n Programme Finished!')
