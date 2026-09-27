class Solution:
    def combinationSum3(self, k, n):
        ans = []

        def dfs(start, path, target):
            if len(path) == k:
                if target == 0:
                    ans.append(path[:])
                return

            for i in range(start, 10):
                if i > target:
                    break

                path.append(i)
                dfs(i + 1, path, target - i)
                path.pop()

        dfs(1, [], n)
        return ans