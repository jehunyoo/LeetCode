class Solution:
    # O(n), O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1
        
        for i in range(len(nums)):
            answer.append(product)
            product *= nums[i]
        
        product = 1
        
        for i in range(len(nums) - 1, 0 - 1, -1):
            answer[i] *= product
            product *= nums[i]
        
        return answer
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = nums.count(0)
        if zeros > 2:
            return [0 for _ in nums]
        elif zeros == 1:
            index = nums.index(0)
            for num in nums:
                if num != 0:
                    product *= num
            return [product if index == idx else 0 for idx, _ in enumerate(nums)]
        else:
            answer = []
            for num in nums:
                answer.append(product)
                product *= num
            product = 1
            for idx, num in enumerate(nums[::-1]):
                answer[-(idx+1)] *= product
                product *= num
            return answer

    # with division
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        product_all = 1
        zeros = nums.count(0)
        if zeros == 0:
            for num in nums:
                product_all *= num
            return [product_all // num for num in nums]
        elif zeros == 1:
            for num in nums:
                if num != 0:
                    product_all *= num
            index = nums.index(0)
            return [product_all if idx == index else 0 for idx, _ in enumerate(nums)]
        else:
            return [0 for _ in nums]
