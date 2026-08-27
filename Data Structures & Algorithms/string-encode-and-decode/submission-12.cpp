class Solution {
public:

    string encode(vector<string>& strs) {
        string str = "";

        for (int i = 0; i < strs.size(); i++) {
            int str_length = strs[i].length();

            str += to_string(str_length);
            str += "#";
            str += strs[i];
        }

        return str;
    }

    vector<string> decode(string s) {
        vector<string> res;

        int i = 0;
        while (i < s.length()) {
            int j = i;

            while (s[i] != '#') {
                i += 1;
            }

            int str_length = stoi(s.substr(j, i - j));

            res.push_back(s.substr(i + 1, str_length));

            i += str_length + 1;
        }

        return res;
    }
};
