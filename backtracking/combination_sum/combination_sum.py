class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr_sum, curr_path):
            if curr_sum == target:
                res.append(curr_path[:])
                return
            
            if curr_sum > target:
                return

            for i in range(start, len(nums)):
                curr_path.append(nums[i])
                backtrack(i, curr_sum + nums[i], curr_path)
                curr_path.pop()

        backtrack(0, 0, [])
        return res

    


        