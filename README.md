# Simple Flask Blog App  

This is a **simple blog application** built using Flask. The app allows users to **create, edit, and view blog posts**. It includes an admin panel for adding new posts, a homepage displaying all posts, and individual post pages.

---

## 📌 Features  
✔️ **Create Posts** – Users can add blog posts with images.  
✔️ **Edit Posts** – Existing posts can be updated.  
✔️ **View Posts** – Posts are displayed on the homepage and can be viewed individually.  
✔️ **Flash Messages** – Users get notifications for actions like creating or updating posts.  
✔️ **Simple ID System** – Automatically assigns and reverses post order.  

---

## 🚀 Installation  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/asliddintursunoff/Simple-Blog-Post-Flask-application.git
cd Simple-Blog-Post-Flask-application
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

---

## ⚙️ Usage  

### **Run the Flask Application**  
```sh
python app.py
```
The app will be available at: **`http://127.0.0.1:5000/`**  

---



---

## 🛠 API Routes  

| Route | Method | Description |
|--------|--------|-------------|
| `/` | GET | Displays the homepage with all posts |
| `/admin` | GET, POST | Admin page to create new posts |
| `/<int:id>` | GET, POST | Edit a specific post |
| `/post/<int:id>` | GET | View a single post |

---






