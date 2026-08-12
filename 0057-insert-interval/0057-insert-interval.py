class Solution:
    def insert(self, intervals, newInterval):
        result = []
        s, e = newInterval

        for cs, ce in intervals:
            if ce < s:
                result.append([cs, ce])
            elif cs > e:
                result.append([s, e])
                s, e = cs, ce
            else:
                s = min(s, cs)
                e = max(e, ce)

        result.append([s, e])
        return result
