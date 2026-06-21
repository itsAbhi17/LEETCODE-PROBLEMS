from typing import List
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))       # original edge
            graph[v].append((u, 2 * w))   # reversed usage

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]