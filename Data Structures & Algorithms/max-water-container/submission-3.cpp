class Solution {
public:
    int maxArea(vector<int>& heights) {
        int res = 0;

        int l = 0;
        int r = heights.size() - 1;

        while (l < r) {
            int min_height = min(heights[r], heights[l]);

            res = max(res, min_height * (r - l));

            if (heights[r] < heights[l]) {
                r -= 1;
            } else {
                l += 1;
            }
        }

        return res;
    }
};
