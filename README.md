# 🏥 Hospital Management System

> A Python-based hospital management web application built with OOP and Flask.

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-green)](https://flask.palletsprojects.com)

---

## 📌 What is this?

A complete hospital management system that handles three types of patients — Normal, Covid and ICU — with a live web dashboard, severity detection, and data persistence.

Built entirely from scratch using Object Oriented Programming principles.

---

## ✨ Features

- ➕ Add Normal, Covid and ICU patients through a web form
- 🚨 Automatic severity detection based on symptoms, oxygen levels and ventilator status
- 💉 Blood group validation — only accepts real blood groups
- 📊 Live dashboard — total patients, critical, serious and mild counts
- 🎨 Colour coded severity labels and patient type badges
- 💾 JSON persistence — all data saved and loaded automatically
- ⚠️ Custom 404 error page

---

## 🧠 OOP Concepts Used

| Concept | How it's used |
|---|---|
| Classes & Objects | Patient, CovidPatient, ICUPatient |
| Encapsulation | Private symptoms and blood group with getters/setters |
| Inheritance | CovidPatient and ICUPatient extend Patient |
| Polymorphism | check_severity() behaves differently per patient type |

---

## 🛠️ Tech Stack

- **Python 3.13**
- **Flask** — web framework
- **JSON** — data persistence
- **HTML & CSS** — frontend templates
- **Git & GitHub** — version control

---

## 🚀 How to Run

**Step 1 — Clone the repo**
```bash
git clone https://github.com/BisenHarshil/Hospital-Management-System.git
cd Hospital-Management-System
```

**Step 2 — Install Flask**
```bash
pip install flask
```

**Step 3 — Run the app**
```bash
python h_app.py
```

**Step 4 — Open in browser**
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
Hospital-Management-System/
├── h_app.py          — Flask routes and web application
├── hospital.py       — Patient, CovidPatient, ICUPatient classes
├── patient.json      — Saved patient data
└── templates/
    ├── index.html        — Dashboard
    └── add_patient.html  — Add patient form
```

---

## 👨‍💻 Built By

**Harshil Bisen**
Class 10 · PM Shri Kendriya Vidyalaya
Built as part of a 21-day hackathon preparation — from scratch, no templates, no shortcuts.

---

*First project in a series of 3 built during hackathon preparation.*
