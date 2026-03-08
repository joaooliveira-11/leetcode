from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    diff_dict = {}

    for i in range(len(nums)):
        if nums[i] in diff_dict:
            return [diff_dict[nums[i]], i]

        diff_dict[target - nums[i]] = i

    return []  
