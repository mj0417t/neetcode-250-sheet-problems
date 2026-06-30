class Solution:

    # def encode(self, strs: list[str]) -> str:
    #     if not strs:
    #         return '_)'
    #     return '_0'.join(strs)

    # def decode(self, s: str) ->list[str]:
    #     if s=='_)':
    #         return []
    #     res=s.rsplit('_0')
    #     return res

    # def encode(self, strs: list[str]) -> str:
    #     sizes,res=[],''
    #     for s in strs:
    #         sizes.append(len(s))
    #     for size in sizes:
    #         res+=str(size)
    #         res+=','
    #     res+='#'
    #     for s in strs:
    #         res+=s
    #     return res


    # def decode(self, s: str) ->list[str]:
    #     sizes,res,i=[],[],0
    #     while s[i]!='#':
    #         curr=''
    #         while s[i]!=',':
    #             curr+=s[i]
    #             i+=1
    #         sizes.append(int(curr))
    #         i+=1
    #     i+=1
    #     for size in sizes:
    #         res.append(s[i:i+size])
    #         i+=size
    #     return res

    def encode(self, strs: list[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res


    def decode(self, s: str) ->list[str]:
        i,res=0,[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res

if __name__=='__main__':
    strs=['love','your','gameboy']
    # strs=[]
    sol=Solution()
    s=sol.encode(strs)
    print(s)
    print(sol.decode(s))
