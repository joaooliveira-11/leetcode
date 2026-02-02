from typing import List

# You should aim for a solution with O(n) time and O(n) space
# where n is the size of the input array.
def topKFrequent(nums: List[int], k: int) -> List[int]:
    n_count = {}

    for n in nums:
        n_count[n] = n_count.get(n, 0) + 1

    # previously instead of an array I used an auxiliary dict to do the frequency part
    # the problem is that I had to iterate backwards and did a .keys().__reversed()
    # which might not be optimal
    # for this case, using an array simplifies this process
    freq = [[] for i in range(len(nums) + 1)]
    for n in n_count:
        freq[n_count[n]].append(n)

    answ = []
    for i in range(len(freq) - 1, 0, -1):
        if len(freq[i]) == 0:
            continue
        left = k - len(answ)
        if left == 0:
            return answ
        answ.extend(freq[i][:left + 1])
    return answ

if __name__ == "__main__":
    print(topKFrequent(nums = [1,2,2,3,3,3], k = 2))
    print(topKFrequent(nums = [7,7], k = 1))