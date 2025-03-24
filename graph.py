class ResourceAllocationGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append(to_node)

    def detect_cycle_util(self, node, visited, stack):
        visited.add(node)
        stack.add(node)

        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                if self.detect_cycle_util(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True  # Cycle detected

        stack.remove(node)
        return False

    def detect_cycle(self):
        visited = set()
        stack = set()

        for node in self.graph:
            if node not in visited:
                if self.detect_cycle_util(node, visited, stack):
                    return True
        return False

    def break_cycle(self):
        """Removes an edge from the first detected cycle to resolve deadlock"""
        if not self.detect_cycle():
            return

        print("Breaking cycle by removing an edge...")
        for node in list(self.graph.keys()):
            if self.graph[node]:
                self.graph[node].pop()  # Remove one dependency to break cycle
                break
