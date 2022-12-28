''' Question:

Given an array of sorted numbers and a target sum,
find a pair in the array whose sum is equal to the given target.

Write a function to return the two numbers (i.e. the pair)
such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [2, 4]
Explanation: The numbers 2 & 4 add up to 6: 2 + 4 = 6


Example 2:

Input: [2, 5, 9, 11], target=11
Output: [2, 9]
Explanation: The numbers 2 & 9 add up to 11: 2 + 9 = 11

'''




// Possible Solution 1

// N^2 time complexity ... 0(1) space -> brute force approach

function targetSumPair(arr, target_sum) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] == target_sum) {
        return [arr[i],arr[j]]
      }
    }
  }
  // error case, if no solution is possible
  return [-1, -1];
}




// Possible Solution 2

// hash table approach
// The time complexity is O(N), where ‘N’ is the total number of elements in the input array.

// The space complexity is O(N) -> worst case is ‘N’ numbers in the hash table.

function targetSumPair(arr, target) {
    const seen = {}
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] in seen) {
            return [target - arr[i], arr[i]]
        }
        seen[target - arr[i]] = i
    }
    return [-1, -1]
}




// Possible Solution 3

// a more optimal way to solve this taking advantange of the array being sorted
// Two pointer approach
  // O(n) time
  // 0(1) space