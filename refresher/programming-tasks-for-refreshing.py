from utils import printQuestion

try:
  # Assignment Solution:

    # 1. Calculate the Area of a Rectangle:
    Q_1 = 'Area of a Rectangle'
    printQuestion(Q_1)

    rectLen = int(input('Enter the length of the rectangle: '))
    rectWidth = int(input('Enter the width of the rectangle: '))

    rectArea = rectLen * rectWidth

    print(f'\nThe area of the rectangle is: {rectArea}')

    # 2. Check if a Number is Even or Odd:
    Q_2 = 'Check if a Number is Even or Odd'
    printQuestion(Q_2)

    num = int(input('Enter a number: '))
    isDivisibleBy2 = num % 2 == 0

    print(f'{num} is even') if bool(isDivisibleBy2) else print(f'{num} is odd')

    # 3. Reverse a String:
    Q_3 = 'Reverse a String'
    printQuestion(Q_3)

    strToReverse = input('Enter a string: ')

    def reverse_str(str_):
        strList = list(str_)
        strList.reverse()
        str_ = ''.join(strList)
        return str_

    reversedStr = reverse_str(strToReverse)

    print(f'Reversed string: {reversedStr}')

    # 4. Find the Factorial of a Number:
    Q_4 = 'Find the Factorial of a Number'
    printQuestion(Q_4)

    num = int(input('Enter a number: '))

    class Factorial:
        """This is a simple class to calculate the factorial with 2 different methods"""

        def getFactorial_recursiveMethod(self, num):
            if num <= 1:
                return 1
            else:
                return num * self.getFactorial_recursiveMethod(num-1)

        def getFactorial_loopMethod(self, num):
            numsList = [i for i in range(num)]
            numsList.reverse()

            for i in numsList:
                if i < 1:
                    break

                num = num * i

            return num

    factorial = Factorial()

    loopFactorial = factorial.getFactorial_loopMethod(num)
    recursiveFactorial = factorial.getFactorial_recursiveMethod(num)

    print(f'factorial({num}) using Recursive Method', recursiveFactorial)
    print(f'factorial({num}) using Loop Method', loopFactorial)

    print('Recusive Method\'s result = Loop Method\'s result:',
          recursiveFactorial == loopFactorial)

    # 5. Check if a String is Palindrome or Not:
    Q_5 = 'Check if a String is Palindrome or Not'
    printQuestion(Q_5)

    string = input('Enter a string: ')

    def isPalindrome(str_):
        str_ = str_.lower()
        if str_ == reverse_str(str_):
            return True
        else:
            False

    print(f'{string} is a palindrome.') if isPalindrome(
        string) else print(f'{string} is not a palindrome.')

    # 6. Generate Fibonacci Series up to n terms:
    Q_6 = 'Generate Fibonacci Series up to n terms'
    printQuestion(Q_6)

    noOfTerms = int(input('Enter the number of terms: '))

    def fibonacci(n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        return fibonacci(n-1) + fibonacci(n-2)

    def fibonacciSeries(n):
        fibonacciList = []

        for term in range(n+1):
            fn = fibonacci(term)
            fibonacciList.append(fn)

        return fibonacciList

    fibonacciNum = fibonacci(noOfTerms)
    fibonacci_series = fibonacciSeries(noOfTerms)

    print(f'Fibonacci no. equal to the no. of terms, {
          noOfTerms} is {fibonacciNum}')
    print('and')
    print(f'Fibonacci Series up to {noOfTerms} terms is', fibonacci_series)

    # 7. Find the Largest Among Three Numbers:
    Q_7 = 'Find the Largest Among Three Numbers'
    printQuestion(Q_7)

    numerals = input('Enter three numbers separated by space: ')
    numerals = numerals.split(' ')

    def findLargestnumber(seq_):
        numsList = []
        for num in seq_:
            numsList.append(int(num))

        numsList.sort(reverse=True)

        return numsList[0]

    if numerals.__len__() < 3:
        raise ValueError(
            f'Expected minimum 3 nums but found only {len(numerals)}')
    else:
        largestNum = findLargestnumber(numerals)
        print(f'The largest number is: {largestNum}')

    # Calculate Simple Interest:
    Q_8 = 'Calculate Simple Interest'
    printQuestion(Q_8)

    P = int(input('Enter the principal amount: '))
    r = int(input('Enter the rate of interest: '))
    n = int(input('Enter the time period in years: '))

    def simpleInterest(p, n, r):
        r = r/100
        return P*n*r

    I = simpleInterest(P, n, r)

    print(f'Simple Interest: {I}')

    # Convert Celsius to Fahrenheit:
    Q_9 = 'Convert Celsius to Fahrenheit'
    printQuestion(Q_9)

    celsius = input('Enter temperature in Celsius: ')
    celsius = int(celsius)

    """
    "Celsius to Fahrenheit"
    * Multiply the Celsius temperature by 9.
    * Divide the result by 5.
    * Add 32 to the result from step 2.
    """

    def celsiusToFahrenheit(c):
        f = (celsius * 9) / 5
        f = f + 32
        return f

    fahrenheit = celsiusToFahrenheit(celsius)

    print(f'Temperature in Fahrenheit: {fahrenheit}')

    # Check Leap Year:
    Q_10 = 'Check Leap Year'
    printQuestion(Q_10)

    yearToCheck = input('Enter a year: ')
    yearToCheck = int(yearToCheck)

    '''
    "Leap Year Determination"
    * A year is a leap year if:
    * It is evenly divisible by 4,
    * But if it is evenly divisible by 100, it must also be evenly divisible by 400 to be a leap year.
    '''

    def leapYear(year):
        divisibleBy4 = year % 4 == 0
        notDivisibleBy100 = year % 100 != 0
        divisibleBy400 = year % 400 == 0

        if divisibleBy4:
            if notDivisibleBy100:
                return True
            elif divisibleBy400:
                return True
            return False
        return False

    print(f'{yearToCheck} is leap year') if leapYear(
        yearToCheck) else print(f'{yearToCheck} is not a leap year')

except Exception as error:
    print(error)
else:
    print('\n Programme Finished!')
