class Solution {
  public int minSubArrayLen(int target, int[] nums) {
      int windowSum = 0, 
      minLength = Integer.MAX_VALUE;
      int windowStart = 0;
      for (int windowEnd = 0; windowEnd < nums.length; windowEnd++) {
          windowSum += nums[windowEnd]; // add the next element
          // shrink the window as small as possible until the 'windowSum' is smaller than 'S'
          while (windowSum >= target) {
              minLength = Math.min(minLength, windowEnd - windowStart + 1);
              windowSum -= nums[windowStart]; // subtract the element going out
              windowStart++; // slide the window ahead
          }
      }

      return minLength == Integer.MAX_VALUE ? 0 : minLength;
  }
}