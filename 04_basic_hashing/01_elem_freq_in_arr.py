from collections import Counter
class Solution:
    def find_freq(self,arr):
        c= Counter(arr)
        for key,val in c.items():
            print(key," ",val)



if __name__=='__main__':
    sol=Solution()
    arr=[10,5,10,15,10,5]
    arr.extend(arr)
    sol.find_freq(arr)
    print(arr)