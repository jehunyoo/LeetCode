class Solution:
    # remove leaves and update leaves from connected branch
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                branch = graph[leaf].pop()
                graph[branch].remove(leaf)
                
                if len(graph[branch]) == 1:
                    new_leaves.append(branch)
            
            leaves = new_leaves

        return leaves

    # DFS, iteration, Time Limit Exceeded
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        roots = []
        min_height = n + 1
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        for root in range(n):
            stack = [(root, 1)]
            visited = collections.defaultdict(int)
            height = 0

            while stack:
                node, h = stack.pop()
                height = max(height, h)
                if not visited[node]:
                    visited[node] = 1
                    for connected in graph[node]:
                        if not visited[connected]:
                            stack.append((connected, h + 1))

            if height == min_height:
                roots.append(root)
            elif height < min_height:
                roots = [root]
                min_height = height
        
        return roots