import tkinter as tk
from tkinter import messagebox
import random
import networkx as nx
import matplotlib.pyplot as plt
from graph import ResourceAllocationGraph
from deadlock_detector import DeadlockDetector

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection Tool")

        self.detector = DeadlockDetector()

        self.label = tk.Label(root, text="Deadlock Detection System", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()

        self.add_data_button = tk.Button(root, text="Generate Random Data", command=self.add_random_data)
        self.add_data_button.pack(pady=5)

        self.detect_button = tk.Button(root, text="Detect Deadlock", command=self.detect_deadlock)
        self.detect_button.pack(pady=5)

        self.resolve_button = tk.Button(root, text="Resolve Deadlock", command=self.resolve_deadlock)
        self.resolve_button.pack(pady=5)

        self.visualize_button = tk.Button(root, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.pack(pady=5)

    def add_random_data(self):
        """Generates random processes and resource dependencies"""
        self.detector.graph.graph.clear()  # Clear previous data
        num_processes = random.randint(3, 5)
        num_resources = random.randint(2, 4)

        processes = [f"P{i}" for i in range(1, num_processes + 1)]
        resources = [f"R{i}" for i in range(1, num_resources + 1)]

        # Randomly assign resources to processes and vice versa
        for _ in range(random.randint(4, 7)):  # Random number of dependencies
            process = random.choice(processes)
            resource = random.choice(resources)
            self.detector.graph.add_edge(process, resource)

            if random.random() < 0.5:  # 50% chance to create a cycle (deadlock risk)
                reverse_process = random.choice(processes)
                self.detector.graph.add_edge(resource, reverse_process)

        messagebox.showinfo("Random Data", "Random process-resource data generated! Click 'Detect Deadlock'.")

    def detect_deadlock(self):
        """Runs deadlock detection algorithm and displays result"""
        if self.detector.detect_deadlock():
            messagebox.showwarning("Deadlock Detected", "⚠️ Deadlock detected! Click 'Resolve Deadlock'.")
        else:
            messagebox.showinfo("No Deadlock", "✅ No deadlock detected.")

    def resolve_deadlock(self):
        """Resolves deadlock by breaking a cycle"""
        if self.detector.detect_deadlock():
            self.detector.resolve_deadlock()
            messagebox.showinfo("Resolved", "✅ Deadlock resolved! Click 'Visualize Graph' to see changes.")
        else:
            messagebox.showinfo("No Deadlock", "No deadlock found to resolve.")

    def visualize_graph(self):
        """Uses NetworkX & Matplotlib to draw the Resource Allocation Graph"""
        G = nx.DiGraph()
        for node in self.detector.graph.graph:
            for neighbor in self.detector.graph.graph[node]:
                G.add_edge(node, neighbor)

        plt.figure(figsize=(5, 4))
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.title("Resource Allocation Graph")
        plt.show()

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = DeadlockGUI(root)
    root.mainloop()
