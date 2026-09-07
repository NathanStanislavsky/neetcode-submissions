class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            int[] freq = new int[26];

            for (int j = 0; j < strs[i].length(); j++) {
                freq[strs[i].charAt(j) - 'a'] += 1;
            }

            List<Integer> list_freq = new ArrayList<>();

            for (int f : freq) {
                list_freq.add(f);
            }

            List<String> group = map.get(list_freq);
            
            if (group == null) {
                group = new ArrayList<>();

                map.put(list_freq, group);
            }

            group.add(strs[i]);

        }

        return new ArrayList<>(map.values());
    }
}
