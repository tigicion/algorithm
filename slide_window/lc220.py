# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

# 如果存在则返回 true，不存在返回 false。

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getk(v):
            return v//(t+1)
        a={}
        for i, j in enumerate(nums):
            b = getk(j)
            # print(i, j, b, a)
            if b in a:
                return True
            elif b-1 in a and abs(j - a[b-1])<=t:
                return True
            elif b+1 in a and abs(j - a[b+1])<=t:
                return True
            else:
                a[b]=j
            if i-k >=0:
                del a[getk(nums[i-k])]
        return False

if __name__ =="__main__":
    print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))