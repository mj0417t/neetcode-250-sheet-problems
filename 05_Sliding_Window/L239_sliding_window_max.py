from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # window=[-num for num in nums[:k]]
        # heapq.heapify(window)
        # res=[-window[0]]
        # l=0
        # for r in range(k,len(nums)):
        #     window.remove(-nums[l])
        #     l+=1
        #     window.append(-nums[r])
        #     heapq.heapify(window)
        #     res.append(-window[0])
        # return res

        # heap=[]
        # output=[]
        # for r in range(len(nums)):
        #     heapq.heappush(heap, (-nums[r],r))
        #     if r>=k-1:
        #         while heap[0][1]<=r-k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output

        ouput=[]
        q=deque()
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if r+1>=k:
                ouput.append(nums[q[0]])
                l+=1
            r+=1
        return ouput

            


if __name__=='__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    nums2 = [1]
    k2 = 1
    sol=Solution()
    print(sol.maxSlidingWindow(nums,k))
    print(sol.maxSlidingWindow(nums2,k2))