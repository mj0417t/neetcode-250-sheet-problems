class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[:k:-1]+nums[:len(nums)-k]
        # k=k%len(nums)
        # nums[:]=nums[-k:]+nums[:-k]

        cnt=0
        start=0
        while cnt<len(nums):
            curr=start
            prev=nums[start]
            while True:
                next=(curr+k)%len(nums)
                nums[next],prev=prev,nums[next]
                curr=next
                cnt+=1
                if curr==start:
                    break
            start+=1



if __name__=='__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol=Solution()
    sol.rotate(nums, k)
    print(nums)