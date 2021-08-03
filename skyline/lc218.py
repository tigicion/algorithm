# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
# 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
from bisect import bisect_left as bi
from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        t = []
        for i in buildings:
            t.append([i[0], i[2], 1])
            t.append([i[1], i[2], -1])
        t.sort(key=lambda a: a[0])
        s=[]
        res=[]
        def minus(a, b):
            t=bi(a, b)
            a.pop(t)
        def add(a, b):
            t=bi(a,b)
            a.insert(t, b)
        for k, i in enumerate(t):
            if i[2]==1:
                add(s, i[1])
            else:
                minus(s, i[1])
            if (k==len(t)-1 or t[k][0]!=t[k+1][0]) and (len(res)==0 or len(s)==0 or s[-1]!=res[-1][1]):
                if len(s)==0:
                    res.append([i[0], 0])
                else:
                    res.append([i[0], s[-1]])
            print(s, res)
        return res

if __name__ == "__main__":
    a= [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(Solution().getSkyline(a))