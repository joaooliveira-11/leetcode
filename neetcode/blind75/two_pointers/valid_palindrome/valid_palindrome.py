

# You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.
def isPalindrome(s: str) -> bool:
    i, j = 0, len(s) -1

    while i != j and i < j:
        if not s[i].isalnum():
            i+=1
            continue
        if not s[j].isalnum():
            j-=1
            continue

        if s[i].lower() != s[j].lower():
            return False
        
        i+=1
        j-=1
    return True

    
if __name__ == "__main__":
    print(isPalindrome(s = "Was it a car or a cat I saw?"))
    print(isPalindrome(s = "tab a cat"))

