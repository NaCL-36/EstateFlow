# EstateFlow - Quick Start Guide

## ⚡ Fastest Way to Run

### **Windows Users:**

**Double-click `run.bat`** in the project folder

That's it! It will:
- Create virtual environment (if needed)
- Install all dependencies
- Start the Flask app
- Open the website automatically

---

## 🔧 Manual Setup (If run.bat doesn't work)

### **Step 1: Check Python Installation**

Open Command Prompt and run:
```cmd
py --version
```

If it shows Python version (3.8+), continue to Step 2.

If you see an error, you need to install Python:
- Download from https://www.python.org
- During installation, **CHECK "Add Python to PATH"**
- Restart your computer

---

### **Step 2: Create Virtual Environment**

```cmd
cd C:\Users\ssm15\Documents\GitHub\EstateFlow
py -m venv venv
venv\Scripts\activate
```

Your command prompt should show `(venv)` at the start.

---

### **Step 3: Install Dependencies**

```cmd
pip install -r requirements.txt
```

Wait for installation to complete (may take 1-2 minutes).

---

### **Step 4: Run the App**

```cmd
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## 🌐 Access the Website

Once running, open your browser to:

| Page | URL |
|------|-----|
| Home | http://localhost:5000 |
| Properties | http://localhost:5000/properties |
| Admin Login | http://localhost:5000/admin/login |
| Admin Dashboard | http://localhost:5000/admin/dashboard |

**Admin Credentials:**
- Username: `admin`
- Password: `admin123`

---

## ❌ Troubleshooting

### "Python not found"
- Uninstall Python completely
- Download fresh from python.org
- **CHECK "Add Python to PATH" during installation**
- Restart computer
- Try again

### "ModuleNotFoundError: No module named 'flask'"
```cmd
# Make sure venv is activated (you see (venv) in prompt)
pip install -r requirements.txt
```

### "Port 5000 already in use"
```cmd
# Kill the existing process and try again
# Or change port in app.py:
# app.run(debug=True, host='0.0.0.0', port=5001)
```

### "Permission denied" errors
- Right-click Command Prompt
- Select "Run as Administrator"
- Try again

---

## 📝 Alternative: Use run.py

If `run.bat` doesn't work:

```cmd
python run.py
```

This does everything automatically.

---

## 🎉 Success!

You should now see:
- ✅ Virtual environment created
- ✅ Dependencies installed
- ✅ Flask server running
- ✅ Website accessible at http://localhost:5000

Enjoy EstateFlow! 🏠
