# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
# 这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，
# 系统会自动报警 。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(nums, s, e):
            l=e-s+1
            dp=[0 for _ in range(l)]
            dp[0]=nums[s]
            dp[1]=max(nums[s],nums[s+1])
            for i in range(2, l):
                dp[i]=max(dp[i-1], dp[i-2]+nums[s+i])
            return dp[-1]
        
        l=len(nums)
        if l<=3:
            return max(nums)
        return max(rob_range(nums, 0, l-2), rob_range(nums, 1, l-1))
    
if __name__=="__main__":
    s=Solution()
    print(s.rob([1,2,3,1]))
