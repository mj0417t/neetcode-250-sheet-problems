from collections import Counter
class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n=len(nums)
        ans=[0]*(n-k+1)
        window=nums[:k]
        cnt=Counter(window)
        for i,j in sorted(cnt.items(), key=lambda x: (-x[1], -x[0]))[:x]:
            ans[0]+=i*j
        
        l=0
        idx=1
        for r in range(k,n):
            cnt[nums[l]]-=1
            if cnt[nums[l]] == 0:
                del cnt[nums[l]]
            l+=1
            cnt[nums[r]]+=1
            for i,j in sorted(cnt.items(), key=lambda x: (-x[1], -x[0]))[:x]:
                ans[idx]+=i*j
            idx+=1
        
        return ans



if __name__=='__main__':
    nums = [1,1,2,2,3,4,2,3]
    k = 6
    x = 2
    nums2 = [3,8,7,8,7,5]
    k2 = 2
    x2 = 2
    sol=Solution()
    print(sol.findXSum(nums,k,x))
    print(sol.findXSum(nums2,k2,x2))