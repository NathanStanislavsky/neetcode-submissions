class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> num_set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            num_set.add(nums[i]);
        }

        int res = 0;

        for (int i = 0; i < nums.length; i++) {
            if (!num_set.contains(nums[i] - 1)) {
                int streak = 1;
                int curr = nums[i] + 1;

                while (num_set.contains(curr)) {
                    streak += 1;
                    curr += 1;
                }

                if (streak > res) {
                    res = streak;
                }
            }
        }

        return res;
    }
}
