class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c == ".":
                continue
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end_of_word = True


    def recursive_search(self, word: str, curr_node: TrieNode, idx: int) -> bool:
        curr = curr_node

        for i in range(idx, len(word)):
            if word[i] == ".":
                for child in curr.children.values():
                    if self.recursive_search(word, child, i + 1):
                        return True
                
                return False
                    
            if word[i] not in curr.children:
                return False
            
            curr = curr.children[word[i]]

        return curr.is_end_of_word

    def search(self, word: str) -> bool:
        return self.recursive_search(word, self.root, 0)
        
