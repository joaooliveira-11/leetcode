def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26 # O(1) space size since it's independent of the input size

    for ss in s:
        count[ord(ss) - ord('a')] += 1

    for tt in t:
        idx = ord(tt) - ord('a')
        count[idx] -= 1
        if count[idx] < 0:
            return False
    
    return True


if __name__ == "__main__":
    print(isAnagram(s = "racecar", t = "carrace"))
    print(isAnagram(s = "jar", t = "jam"))