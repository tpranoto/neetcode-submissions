class Solution {
    public boolean isValid(String s) {
        if(s.length() %2==1){
            return false;
        }

        Stack<Character> paren = new Stack<>();
        for(int idx=0;idx<s.length();idx++){
            if (openingParenthesis(s.charAt(idx))){
                paren.push(s.charAt(idx));
            }else{
                if (paren.isEmpty() || 
                    matcher(paren.pop()) != s.charAt(idx)){
                    return false;
                }
            }
        }
        
        if (!paren.isEmpty()){
            return false;
        }

        return true;
    }

    private boolean openingParenthesis(char c){
        return c == '(' || c == '{' || c == '[';
    }

    private char matcher(char s){
        switch (s){
            case '(':
                return ')';
            case '{':
                return '}';
            case '[':
                return ']';
        }
        return 'x';
    }
}
