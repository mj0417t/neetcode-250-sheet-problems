class StockSpanner:

    def __init__(self):
        self.st=[]

    def next(self, price: int) -> int:
        cnt=1
        while self.st and price>=self.st[-1][0]:
            p,c=self.st.pop()
            cnt+=c
        self.st.append((price,cnt))
        return cnt
        

if __name__=='__main__':
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))
    print(stockSpanner.next(80))
    print(stockSpanner.next(60))
    print(stockSpanner.next(70))
    print(stockSpanner.next(60))
    print(stockSpanner.next(75))
    print(stockSpanner.next(85))
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)