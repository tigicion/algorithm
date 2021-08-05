# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。


from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a={}
        for j, i in enumerate(nums):
            if i in a.keys():
                return True
            else:
                a[i]=1
            if j-k>=0:
                del a[nums[j-k]]  
        return False
    
if __name__=="__main__":
    print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],3))