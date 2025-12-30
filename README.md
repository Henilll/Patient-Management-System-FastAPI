# 🏥 Patient Management System API

#Live Demo https://patient-management-system-fastapi.onrender.com/view

A fully functional **FastAPI-based REST API** to manage patient records with features like **CRUD operations**, **BMI calculation**, **sorting**, and **strong data validation** using **Pydantic**.

---

## 🚀 Features

- ✅ Create patient records  
- 🔍 View all patients or a single patient  
- ✏️ Update patient details (partial updates supported)  
- ❌ Delete patient records  
- 📊 Automatic BMI calculation with health verdict  
- 🔃 Sort patients by **height**, **weight**, or **BMI**  
- 📁 JSON-based persistent storage  
- 🧠 Robust request validation using **Pydantic v2**

---

## 🛠 Tech Stack

- **Backend**: FastAPI  
- **Language**: Python  
- **Validation**: Pydantic  
- **Database**: JSON File (`patients.json`)  
- **Server**: Uvicorn  

---

## 📂 Project Structure

```text
patient-management-system-fastapi/
│
├── main.py
├── patients.json
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Henilll/Patient-Management-System-API.git
cd patient-management-system-fastapi
```

### 2️⃣ (Optional) Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
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

## 🌐 Base URL

```
http://127.0.0.1:8000
```

---

## 📘 API Endpoints

### 🏠 Home
```http
GET /
```

Response:
```json
{
  "message": "Patient Management System API"
}
```

---

### ℹ️ About
```http
GET /about
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

Example:
```http
GET /view/P001
```

---

### ➕ Create Patient
```http
POST /create
```

Request Body:
```json
{
  "id": "P001",
  "name": "Rahul Sharma",
  "city": "Ahmedabad",
  "age": 29,
  "gender": "Male",
  "height": 1.72,
  "weight": 68
}
```

---

### ✏️ Update Patient (Partial Update)
```http
PATCH /edit/{patient_id}
```

Example Body:
```json
{
  "city": "Surat",
  "weight": 70
}
```

---

### ❌ Delete Patient
```http
DELETE /delete/{patient_id}
```

---

### 🔃 Sort Patients
```http
GET /sort?sort_by={field}&ordered={asc|desc}
```

Allowed Fields:
- `height`
- `weight`
- `bmi`

Example:
```http
GET /sort?sort_by=bmi&ordered=desc
```

---

## 📖 API Documentation

FastAPI provides automatic interactive documentation:

### Swagger UI
```
http://127.0.0.1:8000/docs
```

---

## 🔒 Error Handling

- **400** – Bad Request  
- **404** – Patient Not Found  
- **400** – Duplicate Patient ID  

---

## 🧑‍💻 Author

**Henil Bhavsar**  
Computer Engineering Student  
AI / ML Developer  

---

## ⭐ Support

If you found this project helpful:

- ⭐ Star the repository  
- 🍴 Fork it  
- 🛠 Contribute improvements  

---

## 🔮 Future Improvements

- 🔐 JWT Authentication  
- 🐳 Docker Support  
- 🗄 SQLite / PostgreSQL Integration  
- 🧪 Unit Testing  

---

🚀 *Built with FastAPI & Pydantic*
