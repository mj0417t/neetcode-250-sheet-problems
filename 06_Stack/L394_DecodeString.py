class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for char in s:
            if char==']':
                c=''
                while st and st[-1] !='[':
                    c=st.pop()+c
                if st and st[-1]=='[':
                    st.pop()
                    num=''
                    while st and st[-1].isnumeric():
                        num=st.pop()+num
                    c=int(num)*c
                    st.append(c)
                continue
            st.append(char)
        res=''
        while st:
            res= st.pop()+res
        return res

if __name__=='__main__':
    sol=Solution()
    # print(sol.decodeString("3[a]2[bc]"))
    # print(sol.decodeString("3[a2[c]]"))
    # print(sol.decodeString("2[abc]3[cd]ef"))
    print(sol.decodeString("100[leetcode]"))