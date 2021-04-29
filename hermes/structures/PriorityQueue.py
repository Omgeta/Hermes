import heapq


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class PriorityQueue:
    """
    Simple heapq-based min-heap Priority Queue implementation
    """

    def __init__(self):
        self.pq = []
        self.removed = set()
        self.count = 0

    def __len__(self) -> int:
        return self.count

    def insert(self, node: Node):
        """
        Inserts new node into the PQ.

            Parameters:
                node (Node): Node to insert
        """
        entry = node.key, node.value
        if entry in self.removed:
            self.removed.discard(entry)
        heapq.heappush(self.pq, entry)
        self.count += 1

    def minimum(self) -> Node:
        """
        Returns node with minimum weight in the PQ.

            Returns:
                node (Node): Node with minimum weight.
        """
        (priority, item) = heapq.heappop(self.pq)
        node = Node(priority, item)
        self.insert(node)
        return node

    def remove(self, node: Node):
        """
        Removed a given node from the PQ.

            Parameters:
                node (Node): Node to remove
        """
        entry = node.key, node.value
        if entry not in self.removed:
            self.removed.add(entry)
            self.count -= 1

    def decreasekey(self, node: Node, new_priority):
        """
        Modify weight of a node in the PQ.

            Parameters:
                node (Node): Node to modify.
                new_priority (int | float): New priority of the node.
        """
        self.remove(node)
        node.key = new_priority
        self.insert(node)
