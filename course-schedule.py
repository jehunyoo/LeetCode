class Solution:
    # topological sort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1
        
        queue = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        while queue:
            precourse = queue.popleft()
            for course in graph[precourse]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        
        for indegree in indegrees:
            if indegree != 0:
                return False
        return True