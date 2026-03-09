import random

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.indexes = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.append(val)
            self.indexes[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            last_val = self.data[-1]

            val_idx = self.indexes[val]

            self.data[-1] = val
            self.data[val_idx] = last_val
            self.indexes[last_val] = val_idx

            self.data.pop()
            self.indexes.pop(val)

            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()