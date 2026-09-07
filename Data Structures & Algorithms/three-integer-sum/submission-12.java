class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1;
            int r = nums.length - 1;

            while (l < r) {
                while (l < r && l > i + 1 && nums[l] == nums[l - 1]) {
                    l += 1;
                }

                while (l < r && r < nums.length - 1 && nums[r] == nums[r + 1]) {
                    r -= 1;
                }

                if (l >= r) {
                    break;
                }

                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) {
                    res.add(List.of(nums[i], nums[l], nums[r]));
                    l += 1;
                    r -= 1;
                } else if (sum > 0) {
                    r -= 1;
                } else {
                    l += 1;
                }
            }
        }

        return res;
    }
}
