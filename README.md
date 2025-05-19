# 🧪 Insulin Dosing Suite

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Interface](https://img.shields.io/badge/Interface-CLI%20%7C%20GUI-green.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Version](https://img.shields.io/github/v/tag/mattyhakin/insulin-dosing-suite?label=version)
![Release](https://img.shields.io/github/release/mattyhakin/insulin-dosing-suite.svg)
![Tests](https://github.com/mattyhakin/insulin-dosing-suite/actions/workflows/python-ci.yml/badge.svg)
![Last Commit](https://img.shields.io/github/last-commit/mattyhakin/insulin-dosing-suite)
![Repo Size](https://img.shields.io/github/repo-size/mattyhakin/insulin-dosing-suite)

A professional Python-based insulin calculator suite featuring a CLI tool, GUI interfaces, and experimental logic modules to support diabetes management.

---

## 🔍 Overview

This project merges and evolves four earlier tools into a single, modular dosing suite:

- 🛠 **v1.0** – CLI insulin calculator  
- 🧪 **v2.0** – Experimental time-of-day ratio models  
- 🖼 **v3.0** – First Tkinter-based GUI  
- 🚀 **v4.0** – Enhanced GUI with improved layout and UX

---

## 🗂 Project Structure

| Folder         | Purpose                                              |
|----------------|------------------------------------------------------|
| `cli/`         | Command-line based insulin calculator                |
| `gui-v1/`      | First-generation GUI implementation                  |
| `gui-v2/`      | Updated GUI with cleaner layout & usability          |
| `experimental/`| Time-based input models for future exploration       |
| `tests/`       | Unit tests for CLI, GUI, and experimental modules    |

---

## 🚀 Quick Start

### ▶️ CLI Tool
```bash
python cli/main.py
```

### 🖥 GUI App (v2)
```bash
python gui-v2/app.py
```

> Note: GUI v1 is available under `gui-v1/` for legacy reference.

---

## 🧪 Running Tests

Install dependencies:
```bash
pip install -r requirements.txt
```

Then run all tests:
```bash
pytest
```

---

## 📦 Releases

See [RELEASE_NOTES.md](./RELEASE_NOTES.md) for a breakdown of feature evolution.

---

## 📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## 📝 Notes

This repository replaces the following earlier projects:
- [`complexinsulincalc`](https://github.com/mattyhakin/complexinsulincalc)
- [`ratioinputinsulin`](https://github.com/mattyhakin/ratioinputinsulin)
- [`complexinsulincalcGUI`](https://github.com/mattyhakin/complexinsulincalcGUI)
- [`InsulinCalcv3`](https://github.com/mattyhakin/InsulinCalcv3)

They are now archived.
