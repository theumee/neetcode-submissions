class Solution {
    public boolean isPalindrome(String str) {
        String s = str.toLowerCase();
        int i = 0;
        int j = s.length() - 1;
        while(i<j){
            if(!isAlphaNum(s.charAt(i))){
                i++;
                continue;
            }
            if(!isAlphaNum(s.charAt(j))){
                j--;
                continue;
            }
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    static boolean isAlphaNum(char c){
        if((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') ){
            return true;
        }
        return false;
    }
}
