from functools import reduce

# Question.1: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
filtered_fruits = filter(lambda fruit: len(fruit) > 5, fruits)
filtered_fruits = list(filtered_fruits)
print('Fruit-Names with length of Alphabetic Characters more than 5', filtered_fruits)

# Input: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Expected Output: ['banana', 'cherry', 'elderberry']

# Question: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.

nums = [2, 4, 6, 8, 10]
nums_doubled = map(lambda num: num*2, nums)
nums_doubled = list(nums_doubled)
print('Numbers', nums)
print('Doubled Numbers', nums_doubled)

doubled_nums_product = reduce(lambda x, y: x*y, nums_doubled)
print('Doubled Numbers Product', doubled_nums_product)

# Input: [2, 4, 6, 8, 10]
# Expected Output: 122880 (Product of [4, 8, 12, 16, 20])
