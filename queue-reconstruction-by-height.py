class Solution:
    # greedy algorithm, heap, priority queue
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        answer = []
        while heap:
            person = heapq.heappop(heap)
            answer.insert(person[1], [-person[0], person[1]])
        
        return answer
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for h, k in people:
            heapq.heappush(heap, (-h, k))
        
        answer = []
        while heap:
            person = heapq.heappop(heap)
            h, k = -person[0], person[1]

            count = 0
            for i, p in enumerate(answer):
                if count == k:
                    answer.insert(i, (h, k))
                    break
                if p[0] >= h:
                    count += 1
            else:
                answer.append((h, k))
            
        return answer