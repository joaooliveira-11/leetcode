from typing import List

# Follow-up: Could you solve it in O(n) time without using the division operation?
# O(n) time without using the division operation?
# You should aim for a solution as good or better than O(n) time and O(n) space,
# where n is the size of the input array.
def productExceptSelf(nums: List[int]) -> List[int]:
    arr_follow = [0] * len(nums)
    arr_until = [0] * len(nums)

    for i in range(len(nums) -1, -1, -1):
        if i != (len(nums) -1):
            arr_follow[i] = nums[i] * arr_follow[i + 1]
        else:
            arr_follow[i] = nums[i]

    for i in range(len(nums)):
        arr_until[i] = nums[i] * arr_until[i-1] if i > 0 else nums[i]

    answ = [0] * len(nums)
    for i in range(len(nums)):
        if i  == 0:
            answ[i] = arr_follow[i + 1]
        elif i == len(nums)-1:
            answ[i] = arr_until[i - 1]
        else:
            answ[i] = arr_until[i-1] * arr_follow[i+1]

    return answ

if __name__ == "__main__":
    print(productExceptSelf(nums = [1,2,4,6]))  # Output: [48,24,12,8]
    print(productExceptSelf(nums = [-1,0,1,2,3])) # Output: [0,-6,0,0,0]



