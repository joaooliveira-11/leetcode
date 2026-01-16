from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    differences_map = {}

    for i, num in enumerate(nums):
        target_diff = target - num
        target_diff_i = differences_map.get(target_diff) 

        if target_diff_i is not None and target_diff_i != i:
            return [target_diff_i, i]

        differences_map[num] = i
    return []


if __name__ == "__main__":
    print(twoSum(nums = [4,5,6], target = 10))
    print(twoSum(nums = [5,5], target = 10))