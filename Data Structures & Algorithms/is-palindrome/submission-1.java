class Solution {
    public boolean isPalindrome(String str) {
        char[] s = str.toLowerCase().toCharArray();
        int i = 0; 
        int j = s.length-1;
        while(i<=j){
            if(!Character.isLetterOrDigit(s[i])) {
                i++;
                continue;
            }
            if(!Character.isLetterOrDigit(s[j])) {
                j--;
                continue;
            }
            if(s[i] != s[j]) return false;
            i++;
            j--;
            
        }
        return true;
    }
}
