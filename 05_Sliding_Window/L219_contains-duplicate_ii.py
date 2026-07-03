class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, min(len(nums),i+k+1)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        # 
        # using hashmap
        # indices={}
        # for i in range(len(nums)):
        #     idx=indices.get(nums[i],-1)
        #     if idx>-1 and i-idx<=k:
        #         return True
        #     indices[nums[i]]=i 
        # return False 

        #using hashset
        window=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False


if __name__=='__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    sol=Solution()
    ans=sol.containsNearbyDuplicate(nums,k)
    print(ans)