class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record=[]
        for op in operations:
            if op=='C':
                if record:
                    record.pop()
            elif op=='D':
                elem=record[-1]
                record.append(2*elem)
            elif op=='+':
                a=record[-1]
                b=record[-2]
                record.append(a+b)
            else:
                record.append(int(op))
        
        if not record:
            return 0 
        else:
            return sum(record)




if __name__=='__main__':
    # ops1 = ["5","2","C","D","+"]
    ops2 = ["5","-2","4","C","D","9","+","+"]
    ops3 = ["1","C"]
    sol=Solution()
    # print(sol.calPoints(ops1))
    print(sol.calPoints(ops2))
    # print(sol.calPoints(ops3))