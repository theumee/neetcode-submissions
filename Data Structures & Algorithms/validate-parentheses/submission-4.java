class Solution {
    public boolean isValid(String s) {
        final Map<Character, Character> map = Map.of(
            ']','[','}','{',')','('
        );
        Deque<Character> stk = new ArrayDeque<>();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                if(stk.isEmpty() || map.get(ch) != stk.peek()) return false;
                stk.pop();
            }
            else {
                stk.push(ch);
            }
        }
        return stk.isEmpty();
    }
}
