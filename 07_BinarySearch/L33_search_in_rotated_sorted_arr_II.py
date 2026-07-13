class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            #left half sorted
            if nums[l]<nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            #right half sorted
            elif nums[l]> nums[mid]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else: 
                l+=1
        return False

if __name__=='__main__':
    sol=Solution()
    print(sol.search(nums = [2,5,6,0,0,1,2], target = 0))
    print(sol.search(nums = [2,5,6,0,0,1,2], target = 3))