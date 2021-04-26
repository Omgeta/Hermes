import heapq


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.removed = set()
        self.count = 0

    def __len__(self) -> int:
        return self.count

    def insert(self, node: Node):
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)
        heapq.heappush(self.pq, entry)
        self.count += 1

    def minimum(self) -> Node:
        (priority, item) = heapq.heappop(self.pq)
        node = Node(priority, item)
        self.insert(node)
        return node

    def remove(self, node: Node):
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count -= 1

    def decreasekey(self, node, new_priority):
        self.remove(node)
        node.key = new_priority
        self.insert(node)
