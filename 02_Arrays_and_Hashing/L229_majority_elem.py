from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # if len(nums) ==1:
        #     return nums
        # c1=Counter(nums)
        # res=[]
        # for x,y in c1.items():
        #     if y>len(nums)//3:
        #         res.append(x)
        cnt=defaultdict(int)
        for num in nums:
            cnt[num]+=1
            if len(cnt)<=2:
                continue
            new_cnt=defaultdict(int)
            for num,c in cnt.items():
                if c>1:
                    new_cnt[num]=c-1
            cnt=new_cnt
        
        res=[]
        for num in cnt:
            if nums.count(num)>len(nums)//3:
                res.append(num)
        # return res
        return res
if __name__=='__main__':
    sol = Solution()
    nums1 = [3,2,3]
    nums2 = [1,2]
    nums3 = [1]
    print(sol.majorityElement(nums1))
    print(sol.majorityElement(nums2))
    print(sol.majorityElement(nums3))
    