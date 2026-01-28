# EMS
A Django-based Emergency Management System (EMS) that enables citizens to send SOS alerts with live GPS location and allows emergency services to respond quickly through a centralized platform.
# 🚨 Emergency Management System (EMS)

A web-based **Emergency Management System** developed using **Django** to provide fast, reliable, and centralized emergency response during critical situations.

---

## 📌 Problem Statement
Traditional emergency systems rely on phone calls and manual communication, which leads to delays, panic-driven errors, poor location sharing, and lack of coordination between emergency services.

---

## 💡 Solution
This EMS provides:
- One-tap SOS emergency request
- Automatic GPS location sharing
- Centralized emergency dashboard
- Role-based access for services
- Faster response and coordination

---

## 👥 User Roles
- Citizen / Victim
- Emergency Operator
- Admin
- Ambulance Driver
- Police
- Fire Fighter
- Hospital Staff

---

## 🚑 Emergency Types
- Medical Emergency
- Road Accident
- Fire Emergency
- Crime Emergency
- Natural Disaster

---

## ⭐ Key Features
- SOS alert system
- Live GPS location capture
- Emergency request tracking
- Admin monitoring dashboard
- Service assignment workflow
- Secure role-based access

---

## 🛠 Technology Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite / PostgreSQL
- Maps: Google Maps / OpenStreetMap

---

## 🧱 Project Structure



ems/
├── accounts/
├── dashboard/
├── emergencies/
├── services/
├── ems/
├── manage.py
└── README.md


## ▶️ How to Run
```bash
python manage.py migrate
python manage.py runserver
