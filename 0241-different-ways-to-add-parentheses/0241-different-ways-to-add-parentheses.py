from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(expr):
            res = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])

                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)

            # Base case: expr is a number
            if not res:
                res.append(int(expr))

            return res

        return solve(expression)