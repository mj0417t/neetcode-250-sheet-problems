class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs=[(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)

        st=[]
        for p,s in pairs:
            st.append((target-p)/s)
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        return len(st)

if __name__=='__main__':
    sol=Solution()
    print(sol.carFleet(target = 10, position = [3], speed = [3]))
    print(sol.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))
    print(sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))