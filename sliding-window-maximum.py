class Solution:
    # O(n), without max(), queue : Accepted
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        window = collections.deque()
        
        left = 0
        for right in range(len(nums)):
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            window.append(right)
            
            if left > window[0]:
                window.popleft()
            
            if right >= k - 1:
                answer.append(nums[window[0]])
                left += 1
        
        return answer

    # O(n) : Time Limit Exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

    # O(n), less max() : Time Limit Exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index = -1
        answer = []
        for left in range(len(nums) - k + 1):
            right = left + k - 1
            if index < 0:
                index = max(range(k - 1, -1, -1), key=lambda x: nums[left + x])
                maximum = nums[left + index]
            elif index >= 0 and maximum > nums[right]:
                pass
            elif index >= 0 and maximum <= nums[right]:
                index = right - left # == k-1
                maximum = nums[right]
            
            answer.append(maximum)
            index -= 1
        
        return answer
    
    # O(n), less max(), queue : Time Limit Exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        window = collections.deque()
        maximum = float('-inf')
        
        for index, num in enumerate(nums):
            window.append(num)
            if index < k - 1:
                continue
            
            if maximum == float('-inf'):
                maximum = max(window)
            elif maximum < num:
                maximum = num
            answer.append(maximum)
            
            if maximum == window.popleft():
                maximum = float('-inf')
            
        return answer