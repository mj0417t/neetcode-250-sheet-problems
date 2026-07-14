class Solution:
    def get_kth(self,a:list[int], m:int, b:list[int], n:int, k:int, a_strt:int=0, b_strt:int=0)-> int:
        if m>n:
            return self.get_kth(b,n,a,m,k,b_strt,a_strt)
        if m==0:
            return b[b_strt+k-1]
        if k==1:
            return min(a[a_strt],b[b_strt])
        i=min(m,k//2)
        j=min(n,k//2)

        if a[a_strt+i-1]<=b[b_strt+j-1]:
            return self.get_kth(a,m-i,b,n,k-i,a_strt+i,b_strt)
        else:
            return self.get_kth(a,m,b,n-j,k-j,a_strt,b_strt+j)
            
    
    def findMedianSortedArrays(self, nums1: list[int], nums2: List[int]) -> float:
        # BruteForce
        # l=r=0
        # res=[]
        # while l<len(nums1) and r<len(nums2):
        #     if nums1[l]<=nums2[r]:
        #         res.append(nums1[l])
        #         l+=1
        #     else:
        #         res.append(nums2[r])
        #         r+=1
        # while l<len(nums1):
        #     res.append(nums1[l])
        #     l+=1
        # while r<len(nums2):
        #     res.append(nums2[r])
        #     r+=1
        # n=len(res)
        # if n%2 !=0:
        #     return float(res[n//2])
        # else:
        #     return (res[n//2-1]+res[n//2])/2

        
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0


if __name__=='__main__':
    sol=Solution()
    print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
    print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))