class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;

        int res = 0;

        Map<Character, Integer> window_freq = new HashMap<>();
        
        int max_freq = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);

            window_freq.put(c, window_freq.getOrDefault(c, 0) + 1);

            max_freq = Math.max(max_freq, window_freq.get(c));

            while ((r - l + 1) - max_freq > k) {
                char lc = s.charAt(l);

                window_freq.put(lc, window_freq.get(lc) - 1);

                l += 1;
            }

            res = Math.max(res, r - l + 1);            
        }

        return res;
    }
}
