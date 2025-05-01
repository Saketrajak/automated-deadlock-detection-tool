# Automated Deadlock Detection Tool

🔗 **Author 1:** [Saket Rajak 12306983](https://github.com/saketrajak) \
🔗 **Author 2:** [Sarthak Singh 12314993](https://github.com/saketrajak)



# Deadlock Detection Tool

A modern GUI-based tool for detecting deadlocks in operating systems using the Banker's algorithm. This tool provides a visual representation of the resource allocation graph and helps identify potential deadlocks in the system.

## Features

- Interactive GUI for inputting process and resource information
- Real-time visualization of the resource allocation graph
- Deadlock detection using the Banker's algorithm
- Visual representation of process-resource relationships
- Clear indication of deadlocked processes

## Installation

1. Make sure you have Python 3.7+ installed on your system
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python deadlock_detector.py
```

2. Enter the number of processes and resources
3. Click "Initialize Matrices" to create input fields for:
   - Allocation Matrix: Current resource allocation for each process
   - Maximum Need Matrix: Maximum resources needed by each process
   - Available Resources: Currently available resources

4. Fill in the matrices with your system's data
5. Click "Detect Deadlock" to analyze the system state

## Understanding the Graph

- Blue nodes represent processes (P0, P1, etc.)
- Green nodes represent resources (R0, R1, etc.)
- Blue edges show current resource allocation
- Red edges show resource requests
- Edge labels indicate the number of resources

## Example

For a system with:
- 3 processes
- 3 resources
- Available resources: 3,3,2

You would enter:
- Number of Processes: 3
- Number of Resources: 3
- Available Resources: 3,3,2

Then fill in the allocation and maximum need matrices accordingly.

## Requirements

- Python 3.7+
- tkinter
- ttkthemes
- networkx
- matplotlib
- numpy 
