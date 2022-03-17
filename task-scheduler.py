class Solution:
    # greedy algorithm, priority queue(counter.most_common)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        counter = collections.Counter(tasks)
        
        while True:
            not_idle = 0
            for task, _ in counter.most_common(n + 1):
                answer += 1
                not_idle += 1
                counter.subtract(task)
                counter += collections.Counter()
            
            if not counter:
                break
            
            answer += n + 1 - not_idle

        return answer