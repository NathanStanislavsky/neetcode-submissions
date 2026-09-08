class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        Map<Character, Character> closeToOpen = Map.of(
            ')', '(',
            ']', '[',
            '}', '{'
        );

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (closeToOpen.containsKey(c)) {;
                if (stack.isEmpty() || stack.removeLast() != closeToOpen.get(c)) {
                    return false;
                }
            } else {
                stack.addLast(c);
            }
        }

        return stack.isEmpty();
    }
}
