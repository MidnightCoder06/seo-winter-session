iven an array of distinct positive integers representing coin denominations and a singel non-negative integer `n` represening a target amount of money, write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations.

Note taht you can access unlimited amount of coins. In other words, if the denominations are [1,5,10], you have access to an unlimited amount of 1s, 5s and 10s.

If its impossible to make change for the target amount, return -1.

Sample Input:

n = 7
denoms = [1,5,10]


Sample Output
3 

explanation:
2x1 + 1x5 

Optmal space & time complexity:

0(n *d) time

0(n) space

n is the target amount and d is the number of coin denominations

