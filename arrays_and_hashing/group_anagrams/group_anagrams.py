from typing import List

# Recommended Time and Complexity
# You should aim for a solution with O(m * n) time and O(m) space,
# where m is the number of strings and n is the length of the longest string.

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        
    group_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            k = ord(c) - ord('a')
            count[k] += 1
        key = tuple(count)

        group_dict[key].append(s)

    return list(group_dict.values())
