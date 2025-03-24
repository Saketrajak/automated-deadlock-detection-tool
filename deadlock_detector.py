from graph import ResourceAllocationGraph

class DeadlockDetector:
    def __init__(self):
        self.graph = ResourceAllocationGraph()

    def run(self):
        if self.detect_deadlock():
            print("⚠️ Deadlock detected! Resolving...")
            self.resolve_deadlock()
        else:
            print("✅ No deadlock detected.")

    def detect_deadlock(self):
        return self.graph.detect_cycle()

    def resolve_deadlock(self):
        self.graph.break_cycle()
