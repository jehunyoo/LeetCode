class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for departure, arrival, price in flights:
            graph[departure].append((arrival, price))
        
        visited = {}
        heap = [(0, 0, src)]
        
        while heap:
            cost, stop, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if (city not in visited or visited[city] > stop) and stop <= k:
                visited[city] = stop
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost + price, stop + 1, neighbor))
        
        return -1

    # TLE
    # heapq, search all possible route
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    #     graph = collections.defaultdict(list)
    #     for departure, arrival, price in flights:
    #         graph[departure].append((arrival, price))
        
    #     queue = [(0, src, K)]
        
    #     while queue:
    #         cost, city, k = heapq.heappop(queue)
    #         if city == dst:
    #             return cost
    #         if k >= 0:
    #             for arrival, price in graph[city]:
    #                 heapq.heappush(queue, (cost + price, arrival, k - 1))
        
    #     return -1