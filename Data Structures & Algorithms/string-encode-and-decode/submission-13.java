class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder("");

        for (int i = 0; i < strs.size(); i++) {
            int len = strs.get(i).length();

            sb.append(len);
            sb.append("#");
            sb.append(strs.get(i));
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        
        for (int i = 0; i < str.length(); i++) {
            int j = i;

            StringBuilder len = new StringBuilder("");

            while (Character.isDigit(str.charAt(j))) {
                len.append(str.charAt(j));
                j += 1;
            }

            int int_len = Integer.parseInt(len.toString());

            j += 1;

            res.add(str.substring(j, j + int_len));

            i = j + int_len - 1;
        }

        return res;
    }
}
