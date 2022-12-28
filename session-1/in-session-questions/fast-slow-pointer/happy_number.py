
'''
Algorith:

The process, defined above, to find out if a number is a happy number or not, always ends in a cycle.
If the number is a happy number, the process will be stuck in a cycle on number '1'
and if the number is not a happy number then the process will be stuck in a cycle with a set of numbers.
As we saw in Example-2 while determining if '12' is a happy number or not,
our process will get stuck in a cycle with the following numbers:
89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

We saw in the LinkedList Cycle problem that we can use the Fast & Slow pointers method to find a cycle
among a set of elements.
As we have described above, each number will definitely have a cycle.
Therefore, we will use the same fast & slow pointer strategy to find the cycle and once the cycle is found,
we will see if the cycle is stuck on number '1' to find out if the number is happy or not.

'''


class Solution:
    def find_square_sum(self, num):
        _sum = 0
        while (num > 0): # if you do //= 10 on a single digit number it will result in zero
            digit = num % 10 # take the last digit
            _sum += digit * digit # get its square
            num //= 10 # actually chop of the last digit
        return _sum

    def isHappy(self, num: int) -> bool:
        slow, fast = num, num
        while True:
            slow = self.find_square_sum(slow)  # move one step
            fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
            if slow == fast:  # found the cycle
                break
        return slow == 1  # see if the cycle is stuck on the number '1'


'''

Time 
O(logN) ... math is complex but just like how binary search & recursive tree algorithms

Space
O(1)

'''
