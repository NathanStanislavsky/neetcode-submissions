class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> res;

        for (int i = 0; i < nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l += 1;
                    r -= 1;

                    while (l < r && nums[l] == nums[l - 1]) {
                        l += 1;
                    }

                    while (l < r && nums[r] == nums[r + 1]) {
                        r -= 1;
                    }
                } else if (sum < 0) {
                    l += 1;
                } else {
                    r -= 1;
                }
            }
        }

        return res;
    }
};
