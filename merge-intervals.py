class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = []
        for interval in intervals:
            if not answer:
                answer.append(interval)
            else:
                if interval[0] <= answer[-1][1]:
                    start, end = answer.pop()
                    answer.append([start, max(end, interval[1])])
                else:
                    answer.append(interval)

        return answer