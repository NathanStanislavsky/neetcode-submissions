class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> groups;

        for (int i = 0; i < strs.size(); i++) {
            array<int, 26> freq = {};

            for (int j = 0; j < strs[i].length(); j++) {
                freq[strs[i][j] - 'a'] += 1;
            }

            groups[freq].push_back(strs[i]);
        }

        vector<vector<string>> res;

        for (auto& [key, group] : groups) {
            res.push_back(group);
        }

        return res;
    }
};
