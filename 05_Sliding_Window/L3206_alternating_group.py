class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        grps=0
        n=len(colors)
        g1=[1,0,1]
        g2=[0,1,0]
        window=colors[:3]
        if window==g1 or window==g2:
            grps+=1
        for r in range(3,n+2):
            del window[0]
            window.append(colors[r%n])
            if window==g1 or window==g2:
                grps+=1
        return grps


if __name__=='__main__':
    colors = [1,1,1]
    colors2 = [0,1,0,0,1]
    sol=Solution()
    print(sol.numberOfAlternatingGroups(colors))
    print(sol.numberOfAlternatingGroups(colors2))