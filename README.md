
# 🧠 AI for Missing Person Identification

This project leverages AI and facial recognition to identify missing persons using image comparisons. It is built using **Python**, **OpenCV**, **face_recognition**, and **Django**, with a built-in SQLite3 database to store records.

---

## 🚀 Features

- Upload and store images of missing persons and found persons.
- Use AI-based facial recognition to match found persons with database records.
- Real-time image comparison via webcam or uploaded photos.
- Simple UI for uploading and managing data.
- Integrated SQLite3 database for easy deployment.

---

## 🛠️ Tech Stack

- **Backend**: Django, SQLite3
- **AI/ML**: OpenCV, face_recognition
- **Language**: Python
- **Frontend**: HTML (Django templates)

---

## 📦 Requirements

Install the required libraries with:

```bash
pip install -r requirements.txt
```

**Dependencies include**:
- Django
- opencv-python
- face_recognition
- numpy
- dlib
- Pillow

---

## 🧪 Installation and Setup

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/ai-missing-person.git
cd ai-missing-person
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run migrations** (if needed):

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Run the server**:

```bash
python manage.py runserver
```

5. **Access the web app**:

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🖼️ How to Use

1. Upload images of **missing persons** via the web interface.
2. Upload or capture an image of a **found person**.
3. The system compares the image using facial recognition and returns a match result.
4. Admins can view, edit, or delete records through the Django admin panel.

---

## 📁 Project Structure

```
AI for Misiing person/
│
├── db.sqlite3                  # Database file
├── manage.py                   # Django manager
├── requirements.txt            # Dependency list
├── test.py                     # Standalone script for testing recognition
├── testimg.py                  # Script for testing with webcam
├── Help.txt                    # Basic usage/help instructions
├── .idea/                      # IDE config files (PyCharm)
└── [Django App folders]        # Not listed but assumed
```

---

## 📸 Screenshots

*(Add screenshots of the UI and test results if available.)*

---

## 📌 Notes

- The face recognition logic is based on distance measurement between face encodings.
- Webcam access is used for real-time detection.
- `test.py` and `testimg.py` allow independent testing of facial match logic without Django.

---

## 📈 Future Improvements

- Improve UI/UX design.
- Add role-based access (Admin/User).
- Support for cloud-based image storage.
- Mobile-friendly version.
- Better accuracy with deep learning models.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙋‍♂️ Contact

Created by [Your Name](mailto:your.email@example.com) — feel free to contact me!
