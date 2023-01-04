def max_sub_array_of_size_k(input_list, k):
    if k > len(input_list):
        print('invalid input')
        return -1

    max_sub_array_sum = 0
    window_start = 0
    curr_window_sum = 0

    for window_end in range(len(input_list)):
        curr_window_sum += input_list[window_end]  # add the next element
        if(window_end - window_start + 1 == k): # don't slide the window if we haven't achieved the required window size
            max_sub_array_sum = max(max_sub_array_sum, curr_window_sum)
            curr_window_sum -= input_list[window_start]  # subtract the element going out
            window_start += 1  # slide the window forward
    return max_sub_array_sum

print(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3)) # 9
print(max_sub_array_of_size_k([2, 3, 4, 1, 5], 2)) # 7

'''
Time Complexity
O(N)
Space Complexity
O(1)
'''
