# Rishan AI Agents Platform

An Enterprise Agentic AI Workforce with Model Context Protocol (MCP), Microsoft 365, TrekkSoft, and Human-in-the-Loop (HITL) Safety Controls.

---

## 🛠️ Prerequisites

* **Python 3.10+** installed on your system.
* **Visual Studio Code** (VS Code).
* **Python Extension for VS Code** (`ms-python.python`).

---

## 🚀 How to Run in VS Code

### Option 1: One-Click Run via VS Code Debugger (Recommended)
1. Open **VS Code**.
2. Go to **File ➔ Open Folder...** and select this project directory:
   `c:\Users\rr749\OneDrive\Desktop\Claude-Native Agentic AI Business Platform`
3. Press **F5** (or click **Run & Debug** in the sidebar and click the green ▶️ button).
4. Select **`🚀 Run FastAPI Server (Rishan AI)`**.
5. Open your browser and navigate to:
   👉 **`http://127.0.0.1:8000`**

---

### Option 2: Run via VS Code Terminal

1. Open the integrated terminal in VS Code (**Ctrl + `** or `Terminal ➔ New Terminal`).
2. Install dependencies (if not already installed):
   ```bash
   pip install fastapi uvicorn pydantic requests
   ```
3. Run the FastAPI server:
   ```bash
   python src/main.py
   ```
4. Open your browser at:
   👉 **`http://127.0.0.1:8000`**

---

## 🧪 How to Run Tests

In the VS Code Terminal, run:
```bash
python -m unittest discover tests
```

---

## 📁 Key Pages & Architecture

* **Dashboard**: `http://127.0.0.1:8000/dashboard.html` (Main AI Workstation)
* **Team Solutions**: `http://127.0.0.1:8000/team.html?team=revops` (Department View)
* **Explore Apps**: `http://127.0.0.1:8000/explore.html` (9000+ App Directory)
* **Enterprise Hub**: `http://127.0.0.1:8000/enterprise.html` (Governance & Security)
* **Resources**: `http://127.0.0.1:8000/resources.html` (Knowledge Base)
* **Login & Auth**: `http://127.0.0.1:8000/login.html` (Registration & SSO)
