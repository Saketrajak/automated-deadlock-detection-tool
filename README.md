# Automated Deadlock Detection Tool

🔗 **Author 1:** [Saket Rajak 12306983](https://github.com/saketrajak) \
🔗 **Author 2:** [Sarthak Singh 12314993](https://github.com/saketrajak)



## 📌 Overview
The **Automated Deadlock Detection Tool** is a C++ implementation that monitors resource allocation and detects deadlocks in an Operating System environment. It uses a **Resource Allocation Graph (RAG)** to identify cycles and applies deadlock resolution strategies to prevent system crashes.

## ⚙️ Features
- **Real-time Deadlock Detection** using cycle detection in a resource allocation graph.
- **Deadlock Resolution** by preempting processes or releasing resources.
- **Logging System** to track deadlock occurrences.
- **Configurable Process & Resource Allocation** through JSON files.
- **Modular Codebase** for easy expansion.

## 🔧 Installation & Setup
### 1️⃣ Prerequisites
- **C++ Compiler (G++)**
- **CMake (Optional, for easier builds)**

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Saketrajak/automated-deadlock-detection-tool.git
cd deadlock_detector
```
## 🛠️ How It Works
1. **Graph Representation:**
   - Processes and resources are represented as nodes.
   - Edges indicate resource allocation and requests.
2. **Cycle Detection:**
   - Uses **Depth-First Search (DFS)** to identify cycles.
3. **Deadlock Handling:**
   - If a cycle is detected, an alert is raised.
   - The system attempts to resolve the deadlock by releasing resources or terminating processes.
4. **Logging:**
   - Deadlock occurrences are logged for debugging.

## 📝 Configuration
Modify `deadlock_config.json` to set custom resources and processes:
```json
{
    "max_resources": 5,
    "processes": ["P1", "P2", "P3"],
    "resources": ["R1", "R2"]
}
```

## 🚀 Future Enhancements
- GUI visualization of the resource allocation graph.
- Integration with real-time operating systems.
- Advanced deadlock prevention techniques.

## 📜 License
This project is licensed under the MIT License.

## 🙌 Contributing
Pull requests are welcome! If you find a bug or have suggestions, feel free to open an issue.

---

🔗 **Author:** [Saket Rajak](https://github.com/saketrajak)
