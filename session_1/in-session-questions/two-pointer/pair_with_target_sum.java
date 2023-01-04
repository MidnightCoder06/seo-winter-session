
public int[] findPair(int[] array, int target) {
    int[] answer = new int[2];
    int left = 0;
    int right = array.length - 1;

    while (left < right) {
        int currentSum = array[left] + array[right];

        if (currentSum == target) {
            answer[0] = array[left];
            answer[1] = array[right];
            return answer;
        } else if (currentSum < target) {
            left++;
        } else {
            right--;
        }
    }

    return null;
}