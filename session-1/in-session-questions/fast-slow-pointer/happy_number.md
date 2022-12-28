https://leetcode.com/problems/happy-number/description/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true

Explanation:
1 squared  + 9 squared = 82
8 squared + 2 squared = 68
6 squared + 8 squared = 100
1 squared + 0 squared + 0 squared = 1



Example 2:

Input: 12
Output: false (12 is not a happy number)
Explanations: Here are the steps to find out that 12 is not a happy number:


-> 1 squared + 2 squared  = 1 + 4 = 5

-> 5 squared = 25

-> = 4 + 25 = 29

-> = 4 + 81 = 85

-> = 64 + 25 = 89       *****

-> = 64 + 81 = 145

-> = 1 + 16 + 25 = 42

-> = 16 + 4 = 20

-> = 4 + 0 = 4

-> = 16

-> = 1 + 36 = 37

-> = 9 + 49 = 58

-> = 25 + 64 = 89       *****


We hit 89 for the second time.
This means that we are in the wrong loop and can never reach '1'.
Therefore, '12' is not a happy number.





Make sure you're familiar the following operations:

sample_num = 123
concept_one = sample_num / 10
print(concept_one) # 12.3
concept_two = sample_num // 10
print(concept_two) # 12

another_sample_num = 888
another_sample_num //= 10
print(another_sample_num) # 88
another_sample_num //= 10
print(another_sample_num) # 8
another_sample_num //= 10
print(another_sample_num) # 0

final_sample_num = 1489
digit = final_sample_num % 10
print(digit) # 9
print(final_sample_num) # 1489