class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for char in s:
            if char=='(' or char=='{' or char =='[':
                st.append(char)
            else:
                if not st:
                    return False
                if char==')' and st.pop()!='(':
                    return False
                if char=='}' and st.pop()!='{':
                    return False
                if char==']' and st.pop()!='[':
                    return False
        return True if not st else False                
                



if __name__=='__main__':
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([])"
    s5= "([)]"
    sol=Solution()
    print(sol.isValid(s1))
    print(sol.isValid(s2))
    print(sol.isValid(s3))
    print(sol.isValid(s4))
    print(sol.isValid(s5))
    
    
    
    