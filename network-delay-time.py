class Solution:
    # Dijkstra: O(n^2)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = 1000
        graph = [[inf if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]
        for source, target, time in times:
            graph[source][target] = time

        dist = graph[k][:]
        visited = [True] + [False for _ in range(n)]
        visited[k] = True
        
        while not all(visited):
            candidates = []
            for i, v in enumerate(visited):
                if not v:
                    candidates.append(i)
            
            node = min(candidates, key=lambda x: dist[x])
            visited[node] = True
            
            for i, time in enumerate(graph[node]):
                if 0 <= time <= 100 and not visited[i]:
                    dist[i] = min(dist[i], dist[node] + time)
        
        print(dist)
        if max(dist[1:]) > 100:
            return -1
        else:
            return max(dist[1:])
    
    # priority queue (heap)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for target, weight in graph[node]:
                    alt = time + weight
                    heapq.heappush(Q, (alt, target))
        
        if len(dist) == n:
            return max(dist.values())
        else:
            return -1