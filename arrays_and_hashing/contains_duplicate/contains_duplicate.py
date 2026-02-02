from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    aux_dict = {}

    for n in nums:
        n_counter = aux_dict.get(n)
        if n_counter is None:
            aux_dict[n] = 1
            continue
        if n_counter >= 1:
            return True
        aux_dict[n] = n_counter + 1
    return False


if __name__ == "__main__":
    print(hasDuplicate([1, 2, 3, 4]))