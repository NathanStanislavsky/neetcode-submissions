class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;

        for (int i = 0; i < s.length(); i++) {
            freq[s[i]] += 1;
        }

        for (int i = 0; i < t.length(); i++) {
            freq[t[i]] -= 1;
        }

        for (int i = 0; i < freq.size(); i++) {
            if (freq[i] != 0) {
                return false;
            }
        }

        return true;
    }
};
