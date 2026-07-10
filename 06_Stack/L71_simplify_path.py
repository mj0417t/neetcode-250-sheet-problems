class Solution:
    def simplifyPath(self, path: str) -> str:
        # st=[]
        # curr=''
        # for c in path+'/':
        #     if c=='/':
        #         if curr=='..':
        #             if st:
        #                 st.pop()
        #         elif curr !='' and curr!='.':
        #             st.append(curr)
        #         curr=''
        #     else:
        #         curr+=c
        # return '/'+'/'.join(st)

        paths=path.split('/')
        st=[]
        for cur in paths:
            if cur=='..':
                if st:
                    st.pop()
            elif cur!='' and cur!='.':
                st.append(cur)
        return '/'+'/'.join(st)

if __name__=='__main__':
    sol=Solution()
    print(sol.simplifyPath("/home/"))
    print(sol.simplifyPath("/home//foo/"))
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))