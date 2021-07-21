# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _len=len(nums)
        k=_len-k
        if _len<=k:
            return min(nums)
        def part(l, r):
            if l>=r:
                return l
            t=nums[l]
            s=l
            l=l+1
            while l<=r:
                if nums[l]<=t:
                    l+=1
                elif nums[r]>=t:
                    r-=1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
            nums[s], nums[l-1] = nums[l-1], nums[s]
            return l-1

        def qfind(l, r):
            m=part(l,r)
            if m==k:
                return m
            elif m>k:
                return qfind(l, m-1)
            else:
                return qfind(m+1, r)

        res=qfind(0, _len-1)
        return nums[res]

if __name__=="__main__":
    s=Solution()
    print(s.findKthLargest([3,2,1,5,6,4],2))
        