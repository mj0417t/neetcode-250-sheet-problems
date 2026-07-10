class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st=[]
        
        for ast in asteroids:
            flag=True
            while st and st[-1]>0 and ast<0:
                if st[-1]<-ast:
                    st.pop()
                elif st[-1]==-ast:
                    st.pop()
                    flag=False
                    break
                else:
                    flag=False
                    break
                
            if flag:
                st.append(ast)
        return st
            
                

if __name__=='__main__':
    asteroids1 = [5,10,-5]
    asteroids2 = [8,-8]
    asteroids3 = [10,2,-5]
    asteroids4 = [3,5,-6,2,-1,4]
    asteroids5=[-2,2,-1,-2]
    sol=Solution()
    print(sol.asteroidCollision(asteroids1))
    print(sol.asteroidCollision(asteroids2))
    print(sol.asteroidCollision(asteroids3))
    print(sol.asteroidCollision(asteroids4))
    print(sol.asteroidCollision(asteroids5))
    
    
    
    
