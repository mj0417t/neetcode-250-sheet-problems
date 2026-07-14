class Solution:
    
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def findPeak():
            # l=1
            # r=mountainArr.length()-2
            # while l<=r:
            #     mid=(l+r)//2
            #     val1=mountainArr.get(mid-1)
            #     valMid=mountainArr.get(mid)
            #     val2=mountainArr.get(mid+1)
            #     if val1<valMid>val2:
            #         return mid
            #     elif val1<valMid<val2:
            #         l=mid+1
            #     else:
            #         r=mid-1
            # return -1
            l,r=0,mountainArr.length()-1
            while l<=r:
                mid=(l+r)//2
                if mountainArr.get(mid)<mountainArr.get(mid+1):
                    l=mid+1
                else:
                     r=mid-1
            return l
                 
        
        peak=findPeak()
        l,r=0,peak
        while l<=r:
                mid=(l+r)//2
                valMid=mountainArr.get(mid)
                if valMid==target:
                    return mid
                elif valMid<target:
                    l=mid+1
                else:
                    r=mid-1
            

        l,r=peak, mountainArr.length()-1
        while l<=r:
                mid=(l+r)//2
                valMid=mountainArr.get(mid)
                if valMid==target:
                    return mid
                elif valMid<target:
                    r=mid-1
                else:
                    l=mid+1
        return -1