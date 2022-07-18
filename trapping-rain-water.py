class Solution:
    # stack: O(n)
    def trap(self, height: List[int]) -> int:
        rain = 0
        stack = []
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                
                distance = i - stack[-1] - 1
                block = min(height[i], height[stack[-1]]) - height[top]
                rain += distance * block
            
            stack.append(i)
        
        return rain

    # pointers: O(n)
    def trap(self, height: List[int]) -> int:
        rain = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                rain += left_max - height[left]
                left += 1
            else:
                rain += right_max - height[right]
                right -= 1
        
        return rain