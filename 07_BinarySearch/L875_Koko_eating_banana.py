import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            speed=(l+r)//2
            hrs=0
            for pile in piles:
                hrs+= math.ceil(pile/speed)

            if hrs<=h:
                res=speed
                r=speed-1
            else:
                l=speed+1
                
        return res

if __name__=='__main__':
    sol=Solution()
    print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
    print(sol.minEatingSpeed(piles = [312884470], h = 312884469))