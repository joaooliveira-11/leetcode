class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # Dummy nodes to avoid null checks (Head = Oldest, Tail = Newest)
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def add(self, node: Node) -> Node:
        prev, next = self.tail.prev, self.tail
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.val
           
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)

        if(len(self.cache) > self.capacity):
            self.cache.pop(self.head.next.key)
            # del self.cache[self.head.next.key]
            self.remove(self.head.next)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)