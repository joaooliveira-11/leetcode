from typing import List

# Recommended Time and Complexity
# You should aim for a solution with O(m * n) time and O(m) space,
# where m is the number of strings and n is the length of the longest string.

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # key: tuple(array[26]), value: list[anagrams]
    # key: tuple(array[26]), value: list[anagrams]
    anagrams = {}
    for st in strs:
        count = [0] * 26
        for c in st:
            count[ord(c) - ord('a')] +=1
        key = tuple(count)
        if key in anagrams:
            anagrams[key].append(st)
        else:
            anagrams[key] = [st]

    return list(anagrams.values())

if __name__ == "__main__":
    print(groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))

