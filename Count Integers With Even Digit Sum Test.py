'''
2180. Count Integers With Even Digit Sum

Given a positive integer num, return the number of positive integers less than or equal to num
whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

'''

'''
Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.


'''

from typing import List

class Findeven: # Creating class 
    def findevensumofdigits(self,num:int)->List:   # function with input and output parameters
        li =[]
        sum = 0 # for checking sum value as even or not
        
        for i in range(num):
            sum=0
            for digit in str(i):
                sum += int(digit) # finding sum of digits of a number
            
            if int(sum%2) ==0:
                li.append(i)  # fill list with even digit numbers
        return li

findeven = Findeven()
result = findeven.findevensumofdigits(30)
print(result)