
class Solution:
    def sortedSquares(self, input_list: List[int]) -> List[int]:
        result_list = []
        left, right = 0, len(input_list) - 1
        while left <= right:
            if abs(input_list[left]) > abs(input_list[right]):
                result_list.append(input_list[left]**2)
                left += 1
            else:
                result_list.append(input_list[right]**2)
                right -= 1
        return result_list[::-1]

'''
Time complexity
The algorithm's time complexity is O(N). 
We are iterating over the entire input array.

Space complexity
The above algorithm's space complexity is also O(N). 
This is space used for the output array.
'''
