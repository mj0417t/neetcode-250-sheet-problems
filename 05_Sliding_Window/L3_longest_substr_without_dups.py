class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        maxls=1
        for i in range(len(s)):
            charset=set()
            ls=1
            charset.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in charset:
                    break
                else:
                    
                    charset.add(s[j])
                    ls+=1
                    maxls=max(maxls,ls)
        return maxls

if __name__=='__main__':
    sol=Solution()
    s1="abcabcbb"
    s2="bbbbb"
    s3=' '
    print(sol.lengthOfLongestSubstring(s1))
    print(sol.lengthOfLongestSubstring(s2))
    print(sol.lengthOfLongestSubstring(s3))