class Solution:
    # keyword in: O(n), O()
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for stone in stones:
            if stone in jewels:
                answer += 1
        return answer

    # simpler form: O(n), O()
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)
    
    # hashmap (dictionary): O(n), O()
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.defaultdict(int)
        answer = 0
        
        for stone in stones:
            freq[stone] += 1
        for jewel in jewels:
            answer += freq[jewel]
        
        return answer
    
    # collections.Counter: O(n), O()
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        answer = 0
        for jewel in jewels:
            answer += freq[jewel]
        return answer