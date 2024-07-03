import functools

#  Longest Substring Without Repeating Characters

# Description:
# Write a function length_of_longest_substring(str_) that takes a string str_ and
# returns the length of the longest substring without repeating characters.


def length_of_longest_substring(str_: str) -> int:
    # WRITE YOUR CODE HERE

    substrs = []
    temp_str = ''
    for i, char in enumerate(str_):
        if char not in temp_str:
            temp_str += char
        else:
            substrs.append(temp_str)
            temp_str = char
            if i != len(str_)-1:
                continue

        if i == len(str_)-1:
            substrs.append(temp_str)

    substrs.sort(key=lambda substr: -len(substr))

    if substrs.__len__() > 0:
        print('substrings', substrs)
    else:
        print(substrs.__len__())


# Test Case 1:
# Input: "abcabcbb"
# The longest substring without repeating characters is "abc".
# The length of this substring is 3.
print(length_of_longest_substring("abcabcbb"))  # Expected output: 3

# Test Case 2:
# Input: "bbbbb"
# The longest substring without repeating characters is "b".
# The length of this substring is 1.
print(length_of_longest_substring("bbbbb"))  # Expected output: 1

# Test Case 3:
# Input: "pwwkew"
# The longest substring without repeating characters is "wke".
# The length of this substring is 3.
print(length_of_longest_substring("pwwkew"))  # Expected output: 3

# Test Case 4:
# Input: "abcdef"
# The entire string "abcdef" is without repeating characters.
# The length of this substring is 6.
print(length_of_longest_substring("abcdef"))  # Expected output: 6

# Test Case 5:
# Input: "" (empty string)
# An empty string has no characters, so the length is 0.
print(length_of_longest_substring(""))  # Expected output: 0
