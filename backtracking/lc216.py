# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

# 说明：

# 所有数字都是正整数。
# 解集不能包含重复的组合。
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def bt(l, cur, s):
            if s>=n:
                if s==n and len(l)==k:
                    res.append(list(l))
                else:
                    return
            for i in range(cur, 10):
                if s+i>n:
                    return
                l.append(i)
                bt(l, i+1, s+i)
                l.pop()

        bt([], 1, 0)
        return res

if __name__=="__main__":
    s=Solution()
    print(s.combinationSum3(3, 9))
        
