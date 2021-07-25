// # 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

// # 说明：

// # 所有数字都是正整数。
// # 解集不能包含重复的组合。

package main

import "fmt"

func combinationSum3(k int, n int) (ans [][]int) {
	var temp []int
	var dfs func(cur, rest int)
	dfs = func(cur, rest int) {
		// 找到一个答案
		if len(temp) == k && rest == 0 {
			ans = append(ans, append([]int(nil), temp...))
			return
		}
		// 剪枝：跳过的数字过多，后面已经无法选到 k 个数字
		if len(temp)+10-cur < k || rest < 0 {
			return
		}
		for i := cur; i < 10; i++ {
			// 选当前数字
			temp = append(temp, i)
			dfs(i+1, rest-i)
			temp = temp[:len(temp)-1]
		}

	}
	dfs(1, n)
	return
}

func main() {
	fmt.Print(combinationSum3(3, 9))
}
