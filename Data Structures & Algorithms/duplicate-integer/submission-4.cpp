class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (int x : nums) {
            auto it = seen.find(x);

            if (it != seen.end()) {
                return true;
            }

            seen.insert(x);
        }

        return false;
    }
};