import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from deadlock_detector import DeadlockDetector

detector = DeadlockDetector()

# Simulate deadlock scenario
detector.graph.add_edge("P1", "R1")
detector.graph.add_edge("R1", "P2")
detector.graph.add_edge("P2", "R2")
detector.graph.add_edge("R2", "P1")  # Circular wait

detector.run()
