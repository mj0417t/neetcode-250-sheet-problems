class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p=q=0
        # res=[]
        # while p<m and q<n:
        #     if nums1[p]<nums2[q]:
        #         res.append(nums1[p])
        #         p+=1
        #     else:
        #         res.append(nums2[q])
        #         q+=1
        
        # while p<m:
        #     res.append(nums1[p])
        #     p+=1

        # while q<n:
        #     res.append(nums2[q])
        #     q+=1
        
        # for i in range(len(res)):
        #     nums1[i]=res[i]

        p=m-1
        q=n-1
        while p>=0 and q>=0:
            if nums1[p]>nums2[q]:
                nums1[p+q+1]=nums1[p]
                p-=1
            else:
                nums1[p+q+1]=nums2[q]
                q-=1
        while p>=0:
            nums1[p+q+1]=nums1[p]
            p-=1
        while q>=0:
            nums1[p+q+1]=nums2[q]
            q-=1


if __name__=='__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol=Solution()
    sol.merge(nums1,m,nums2,n)
    print(nums1)
        