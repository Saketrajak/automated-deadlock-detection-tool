class ResourceManager:
    def __init__(self):
        self.allocations = {}

    def allocate_resource(self, process, resource):
        print(f"Allocating resource {resource} to process {process}")
        self.allocations[process] = resource

    def release_resource(self, process):
        if process in self.allocations:
            print(f"Releasing resource {self.allocations[process]} from process {process}")
            del self.allocations[process]
