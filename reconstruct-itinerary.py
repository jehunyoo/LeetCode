class Solution:
    # DFS, recursion
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        graph = collections.defaultdict(list)
        for fr, to in sorted(tickets):
            graph[fr].append(to)
        
        def dfs(fr="JFK"):
            while graph[fr]:
                dfs(graph[fr].pop(0)) # O(size of graph[fr])
            itinerary.append(fr)
        
        dfs()
        return itinerary[::-1]
    
    # DFS, recursion, use list.pop instead of list.pop(0)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        graph = collections.defaultdict(list)
        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)
        
        def dfs(fr="JFK"):
            while graph[fr]:
                dfs(graph[fr].pop()) # O(1)
            itinerary.append(fr)
        
        dfs()
        return itinerary[::-1]
    
    # DFS, iteration
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)
        
        itinerary = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())
        
        return itinerary[::-1]