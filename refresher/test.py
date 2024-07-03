# list1 = ['1', '2', '3']
# list1Str = ''.join(list1)
# print(list1Str)

# str_ = 'hello'
# # splittedStr = str_.split('l')
# splittedStr = list(str_)
# print(splittedStr)

# Q = 'Question!'
# seperator = ['**' for char in Q]

# print(''.join(seperator))
# print(Q)

# strToReverse = 'hello'
# strReversedList = list(strToReverse)
# strReversedList.reverse()
# print(strReversedList)

# my_list = ['apple', 'banana', 'cherry']
# my_list.reverse()
# print(my_list)

# num = 5

# num_list = []
# for i in range(num):
#     num_list.append(i)

# print(num_list)
# num_list.reverse()
# print(num_list)

# factorial = num
# print(factorial)
# for i, num in enumerate(num_list, start=1):
#     if num == 0:
#         break
#     factorial = factorial*num

# print(factorial)

# print([i for i in range(5)], 'Hi')

# noOfTerms = 6


# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     return fibonacci(n-1) + fibonacci(n-2)


# fibonacciNum = fibonacci(noOfTerms)

# fibonacciList = []

# def fibonacciSeries(n):
#     for term in range(n):
#         fn = fibonacci(term)
#         fibonacciList.append(fn)
#         print(fibonacciList)


# fibonacciSeries(noOfTerms)

# print(f'Fibonacci no. equal to the no of terms \'{noOfTerms}\' is \'{
#       fibonacciNum}\' \nand\n Fibonacci Series up to {noOfTerms} terms: {fibonacciList}')

# lst = [1, 2, 3, 5, 4, 7, 6]
# lst.sort(reverse=True)
# print(lst)

# string = '234'
# splittedStr = string.split(' ')
# print(splittedStr)

from functools import reduce

strings = ['flower', 'flow', 'flight', 'fly', 'fleet', 'flurt']

shared_prefixes_dict = {}

for iter in range(len(strings)):
    key = f'str{iter}'
    shared_prefixes_dict[key] = []

    iteratingStr = strings[iter]

    for str_ in strings:
        for index in range(1, len(iteratingStr) + 1):
            prefix = iteratingStr[0:index]
            if iteratingStr != str_:
                if str_.startswith(prefix):
                    print(iteratingStr, f'{prefix}:', str_)
                    shared_prefixes_dict[key].append(
                        prefix)


print(shared_prefixes_dict)

shared_prefixes_in_each_str = [
    list_ for list_ in shared_prefixes_dict.values()]


def reducer(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersectedSet = set1.intersection(set2)
    return list(intersectedSet)


shared_prefixes_in_each_str = reduce(
    reducer, shared_prefixes_in_each_str)

print(shared_prefixes_in_each_str)
