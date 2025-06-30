# 🧾 Employee Management System in Python

This is a **console-based Employee Management Application** developed using Python. It allows users to **add**, **view**, and **update** employee records through a simple, menu-driven interface. All records are stored persistently in a local file named `data.txt`.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Concepts Used:** File Handling, Exception Handling, Control Flow, String Parsing

---

## 💡 Features

### 👤 Add Employee
- Input employee name, age, designation, and salary
- Data is saved in `data.txt`
- Supports multiple entries in a session
- Input validation included

### 📄 Display All Employees
- Reads and displays employee records from `data.txt`
- Automatically calculates a **30% hike** on each salary
- Displays both original and updated salaries

### 💸 Raise Salary
- Search by employee name to update salary
- Edits only the matched record in `data.txt`
- Ensures other data remains unchanged

### 🧭 Menu-Based Navigation
- Interactive menu with options:
  - `1` → Add Employee
  - `2` → Display Employees
  - `3` → Raise Salary
  - `4` → Exit
