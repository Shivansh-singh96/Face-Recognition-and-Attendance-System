# Project Agumentation - Face Recognition Attendance System

## 📦 Project Structure
```
Project Agumentation/
│── Attendance.csv
│── Encodefile.p
│── encode_students.py
│── face_recognition.log
│── face_recognition_gui.py
│── face_recognition_gui2.py
│── Service key.json
│── tempCodeRunnerFile.py
│
├── logo/
│    └── logo.png
│
└── Students/
     ├── 1042.jpg
     ├── 1101.jpg
     ├── 1132.png
     ├── 1145.jpg
     └── 1147.jpg
```

## ⚙️ Setup Guide (Windows)

### 1. Install Required Tools
- **Python 3.8 – 3.11**  
- **Visual Studio Installer → Desktop Development with C++** (for dlib)  
- **CMake >= 3.22**  
- **Git** (optional)

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
If `dlib` fails, install a prebuilt wheel from:  
👉 https://github.com/cgohlke/dlib-wheels

### 4. Encode Student Faces
```bash
python encode_students.py
```
This generates `Encodefile.p`.

### 5. Run Face Recognition
```bash
python face_recognition_gui.py
```
or
```bash
python face_recognition_gui2.py
```

### 6. Output
- Attendance marked in **Attendance.csv**
- Encodings stored in **Encodefile.p**

## 🔑 Notes
- **Students/** → store student images.  
- **logo/logo.png** → your logo.  
- **Service key.json** → Firebase integration (if used).  
- Run scripts **inside Project Agumentation/** folder so paths remain valid.
