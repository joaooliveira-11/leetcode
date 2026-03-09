class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # multiplication until a certain idx
        array_until = [1] * len(nums)
        # multiplication forward a certain idx
        array_forward = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                array_until[i] = nums[i]
            else:
                array_until[i] = array_until[i-1] * nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) - 1:
                array_forward[i] = nums[i]
            else:
                array_forward[i] = nums[i] * array_forward[i+1]

        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = array_forward[i+1]
            elif i == len(nums) -1:
                res[i] = array_until[i-1]
            else:
                res[i] = array_until[i-1] * array_forward[i+1]
        
        return res


        