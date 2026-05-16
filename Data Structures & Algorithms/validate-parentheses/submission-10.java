class Solution {
    public boolean isValid(String s) {
        Stack<Character> list = new Stack<>();
        for(char c: s.toCharArray()){
            if(!list.isEmpty() && (c - list.peek() == 1 || c - list.peek() == 2) ){
                list.pop();
            }else{
                list.add(c);
            }
        }
        return list.isEmpty();
    }
}
