Given an array of distinct positive integers representing coin denominations and a singel non-negative integer `n` represening a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.

Sample Input:

n = 6
denoms = [1, 5]

Sample output:

2 

explanation:
1x1 + 1x5 & 6x1

Optmal space & time complexity:

0(n *d) time

0(n) space

n is the target amount and d is the number of coin denominations