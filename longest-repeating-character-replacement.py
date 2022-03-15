class Solution:
    # collections.Counter
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left = 0
        
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            most = counter.most_common(1)[0][1]
            
            if right - left > most + k:
                counter[s[left]] -= 1
                left += 1
        
        return right - left

    # collections.counter
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left, right = 0, 0
        answer = k
        
        counter[s[0]] += 1
        while left <= right < len(s):
            total = counter.total()
            most = counter.most_common(1)[0][1]
            if total <= most + k:
                answer = max(answer, counter.total())
                right += 1
                if right < len(s):
                    counter[s[right]] += 1
            elif total > most + k:
                counter[s[left]] -= 1
                left += 1

        return answer