class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=buy=sell=0
        for i in range(len(prices)):
            if not sell and not buy and i<len(prices)-1 and prices[i]<prices[i+1]:
                buy=prices[i]
            elif buy and i<len(prices)-1 and prices[i]>prices[i+1]:
                profit+=prices[i]-buy
                buy=0
            elif buy and i==len(prices)-1:
                profit+=prices[i]-buy
        return profit

if __name__=='__main__':
    sol = Solution()
    nums1 = [2,1,2,0,1]
    nums2 = [1,2,3,4,5]
    nums3 = [7,6,4,3,1]
    print(sol.maxProfit(nums1))
    print(sol.maxProfit(nums2))
    print(sol.maxProfit(nums3))
    