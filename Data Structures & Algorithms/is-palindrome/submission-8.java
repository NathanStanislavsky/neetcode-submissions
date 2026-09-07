class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l <= r) {
            while (l <= r && !Character.isLetterOrDigit(s.charAt(l))) {
                l += 1;
            }

            while (l <= r && !Character.isLetterOrDigit(s.charAt(r))) {
                r -= 1;
            }

            if (l > r) {
                break;
            }

            char left_letter = Character.toLowerCase(s.charAt(l));
            char right_letter = Character.toLowerCase(s.charAt(r));

            if (left_letter != right_letter) {
                return false;
            }

            l += 1;
            r -= 1;
        }

        return true;
    }
}
