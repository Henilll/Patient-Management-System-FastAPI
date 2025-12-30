# 🏥 Patient Management System

## 🔗 Live Demos

- **Frontend (UI)**:  
  👉 https://patient-management-systemm.netlify.app/

- **Backend API**:  
  👉 https://patient-management-system-fastapi.onrender.com/view

A fully functional **Patient Management System** built with a **FastAPI backend** and a **hosted frontend UI**, supporting **CRUD operations**, **BMI calculation**, **sorting**, and **robust data validation** using **Pydantic**.

---

## 🚀 Features

### 🖥 Frontend
- Clean and responsive UI  
- Patient creation, update, delete, and view  
- Integrated with FastAPI backend  
- Deployed on **Netlify**

### ⚙️ Backend
- ✅ Create patient records  
- 🔍 View all patients or a single patient  
- ✏️ Update patient details (partial updates supported)  
- ❌ Delete patient records  
- 📊 Automatic BMI calculation with health verdict  
- 🔃 Sort patients by **height**, **weight**, or **BMI**  
- 📁 JSON-based persistent storage  
- 🧠 Strong request validation using **Pydantic v2**

---

## 🛠 Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  
- Netlify (Hosting)

### Backend
- **Framework**: FastAPI  
- **Language**: Python  
- **Validation**: Pydantic  
- **Database**: JSON File (`patients.json`)  
- **Server**: Uvicorn  
- **Hosting**: Render

---

## 📂 Project Structure (Backend)

```text
patient-management-system-fastapi/
│
├── main.py
├── patients.json
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup (Backend)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Henilll/Patient-Management-System-API.git
cd patient-management-system-fastapi
```

### 2️⃣ (Optional) Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn
```

### 4️⃣ Run the Application
```bash
uvicorn main:app --reload
```

---

## 🌐 Base URL (Local)

```
http://127.0.0.1:8000
```

---

## 📘 API Endpoints

### 🏠 Home
```http
GET /
```

---

### 👀 View All Patients
```http
GET /view
```

---

### 🔍 View Patient by ID
```http
GET /view/{patient_id}
```

---

### ➕ Create Patient
```http
POST /create
```

---

### ✏️ Update Patient
```http
PATCH /edit/{patient_id}
```

---

### ❌ Delete Patient
```http
DELETE /delete/{patient_id}
```

---

## 📖 API Documentation

Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 🧑‍💻 Author

**Henil Bhavsar**  
Computer Engineering Student  
Full Stack Developer | AI / ML Enthusiast  

---

🚀 *Built with FastAPI & Pydantic*
