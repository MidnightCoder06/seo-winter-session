'''
Note: The below solution is in python2 !!

You can tell because we are using the sys module to represent a maximum int.
Similar to Integer.MAX_VALUE, or the opposite, Integer.MIN_VALUE in Java.

In Python 2, the maximum value for plain int values is available as sys.maxint:

>>> sys.maxint
9223372036854775807

max_size = sys.maxsize
min_size = -sys.maxsize - 1

In python3 

Note that in Python 3 the int type is basically the same as the long type in Python 2, so the idea of a maximum or minimum int isn't applicable.
The plain int type is unbound.

If you just need a number that's bigger than all others, you can use

float('inf')

in similar fashion, a number smaller than all others:

float('-inf')

You can also

# Import math Library
import math

# Print the positive infinity
print (math.inf)

# Print the negative infinity
print (-math.inf)

'''

import sys

class Solution(object):
    def minSubArrayLen(self, target, input_list):   
        window_sum = 0
        min_length = sys.maxint
        window_start = 0

        for window_end in range(0, len(input_list)):
            window_sum += input_list[window_end]  # add the next element
            # shrink the window as small as possible until the 'window_sum' is smaller than 's'
            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= input_list[window_start]
                window_start += 1
        if min_length == sys.maxint:
            return 0
        return min_length


'''

Time Complexity
The time complexity is O(N).
The outer for loop runs for all elements,
and the inner while loop processes each element only once;
therefore, the time complexity of the algorithm will be O(N+N),
which is asymptotically equivalent to O(N).

Space Complexity
The algorithm runs in constant space O(1).

'''
