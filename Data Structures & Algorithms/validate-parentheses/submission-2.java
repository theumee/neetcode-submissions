class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 == 1) return false;
        final Map<Character, Character> map = Map.of(
            ']','[','}','{',')','('
        );
        Deque<Character> stk = new ArrayDeque<>();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsValue(ch)){
                stk.push(ch);
            }
            else {
                if(stk.isEmpty()) return false;
                if(map.get(ch) != stk.peek()) return false;
                stk.pop();
                }
            
        }
        return stk.isEmpty();
    }
}
