class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            k=(l+r)//2
            reqDays=1
            cap=k
            for pkg in weights:
                cap-=pkg
                if cap<0:
                    reqDays+=1
                    cap=k-pkg
            if reqDays<=days:
                r=k-1
            else:
                l=k+1
        return l


if __name__=='__main__':
    sol=Solution()
    print(sol.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
    print(sol.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
    print(sol.shipWithinDays(weights = [1,2,3,1,1], days = 4))