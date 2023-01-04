

# most effecient solution taking advantange of the list being sorted
def target_sum_pair(input_list, target_sum):
  left_pointer, right_pointer = 0, len(input_list) - 1
  while(left_pointer < right_pointer):
    current_sum = input_list[left_pointer] + input_list[right_pointer]
    if current_sum == target_sum:
      return [input_list[left_pointer], input_list[right_pointer]]
    if target_sum > current_sum:
      left_pointer += 1
    else:
      right_pointer -= 1
  # handle invalid case:
  return [-1, -1]

'''

Time Complexity
The time complexity of the algorithm is O(N), where 'N' is the total number of elements in the given array.

Space Complexity
The algorithm runs in constant space O(1).

'''
