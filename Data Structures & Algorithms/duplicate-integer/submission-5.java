class Solution {
    // public boolean hasDuplicate(int[] nums) {
    //     // Make a separate array to keep track of unique numbers
    //     int[] uniqueNums = new int[nums.length];

    //     // Check if list is contained in uniqueNums,
    //     // then nums must have a repeated number
    //     for (int i = 0; i < nums.length; i++) {
    //         if (!uniqueNums.contains(nums[i])) {
    //             uniqueNums[i] = nums[i];
    //         } else {
    //             return true;
    //         }
    //     }
    //     return false;
    // }

    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> uniqueNums = new HashSet<Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            if (!uniqueNums.contains(nums[i])) {
                uniqueNums.add(nums[i]);
            } else {
                return true;
            }
        }

        return false;
    }
}