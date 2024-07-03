from functools import reduce
from utils import printQuestion
from utils import intList

try:
    # Assignment Solution:

    # 1. Find the Median of Three Numbers:
    Q_1 = 'Find the Median of Odd Sequence'
    printQuestion(Q_1)

    sequence = input('Enter the odd sequence of numbers separated by space: ')
    sequence = sequence.split(' ')

    def Median(seq_):
        seq_ = intList(seq_)
        seq_.sort()
        n = len(seq_)
        item = (n + 1) // 2
        return seq_[item-1]

    if len(sequence) % 2 == 0:
        raise ValueError(f'Expected Odd Sequence of Numbers but found Even!')
    elif len(sequence) < 2:
        raise ValueError(f'Expected the Sequence of Numbers but found only {
                         len(sequence)} number!')
    else:
        median = Median(sequence)
        print(f'Median is: {median}')

    # 2.Count the Number of Words in a Sentence:
    Q_2 = 'Count the Number of Words in a Sentence'
    printQuestion(Q_2)

    sentence = input('Enter a sentence: ')
    words = sentence.split(' ')

    print(f'Number of words: {len(words)}')

    # 3. Calculate the Sum of Digits in a Number:
    Q_3 = 'Calculate the Sum of Digits in a Number'
    printQuestion(Q_3)

    number = input('Enter a number: ')

    def sumOfDigits(num):
        digitsList = list(num)
        digitsList = intList(digitsList)
        sum = reduce(lambda x, y: x + y, digitsList)
        return sum

    print(f'Sum of digits: {sumOfDigits(number)}')

    # 4. Find the Longest Common Prefix in a List of Strings:
    Q_4 = 'Find the Longest Common Prefix in a List of Strings'
    printQuestion(Q_4)

    strings = input('Enter strings separated by space: ')
    strings = strings.split(' ')

    def getLongestCommonPrefix(str_seq):

        shared_prefixes_dict = {}

        iterations = len(str_seq)
        for iteration in range(iterations):
            key = f'str{iteration}'
            shared_prefixes_dict[key] = []

            iteratingStr = str_seq[iteration]

            for str_ in str_seq:
                totalIndices = len(iteratingStr) + 1
                for index in range(1, totalIndices):
                    prefix = iteratingStr[0:index]
                    if iteratingStr != str_:
                        if str_.startswith(prefix):
                            shared_prefixes_dict[key].append(
                                prefix)

        prefixes_shared_by_each_str = [
            list_ for list_ in shared_prefixes_dict.values()]

        def reducer(list1, list2):
            set1 = set(list1)
            set2 = set(list2)
            intersectedSet = set1.intersection(set2)
            return list(intersectedSet)

        prefixes_shared_by_each_str = reduce(
            reducer, prefixes_shared_by_each_str)

        prefixes_shared_by_each_str.sort(
            key=lambda str: -len(str))

        return prefixes_shared_by_each_str[0]

    longestCommonPrefix = getLongestCommonPrefix(strings)

    print('Longest common prefix:', longestCommonPrefix)

    # 5. Check if a Number is a Prime Number:
    Q_5 = 'Check if a Number is a Prime Number'
    printQuestion(Q_5)

    number = input('Enter a number: ')
    number = int(number)

    def isPrime(num):
        for i in range(num):
            if i != 0 and i != 1:
                if num % i == 0:
                    return False
        return True

    print(f'{number} is a prime number.') if isPrime(
        number) else print(f'{number} is not a prime number.')

except Exception as error:
    print(error)
else:
    print('\n Programme Finished!')
