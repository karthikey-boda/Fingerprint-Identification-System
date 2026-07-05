# Fingerprint Identification System

A Fingerprint Identification System developed using **Python, Flask, OpenCV, SQLite, HTML, CSS, and JavaScript**. The system verifies whether an uploaded fingerprint already exists in the database. If the fingerprint is new, it enrolls the fingerprint with the provided Voter ID.

---

## Features

- Upload fingerprint image
- Enter Voter ID
- Detect duplicate fingerprints
- Display registered Voter ID if fingerprint already exists
- Enroll new fingerprints into the database
- ORB feature extraction using OpenCV
- SQLite database for voter records
- Simple and responsive web interface

---

## Technologies Used

### Backend
- Python 3
- Flask
- Flask-CORS
- OpenCV
- NumPy
- SQLite

### Frontend
- HTML5
- CSS3
- JavaScript

---

## Project Structure

```
Fingerprint/
│
├── backend/
│   ├── app.py
│   ├── utils/
│   │   ├── database.py
│   │   ├── enroll.py
│   │   ├── feature_extractor.py
│   │   ├── matcher.py
│   │   └── preprocess.py
│   ├── uploads/
│   ├── processed/
│   ├── templates/
│   └── fingerprint.db
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/karthikey-boda/Fingerprint-Identification-System.git
```

Go into the project directory:

```bash
cd Fingerprint-Identification-System
```

---

## Install Dependencies

```bash
pip install flask flask-cors opencv-python numpy
```

---

## Run the Backend

```bash
cd backend
python app.py
```

Server starts at:

```
http://127.0.0.1:5000
```

---

## Run the Frontend

Open the `frontend/index.html` file in your browser.

---

## How It Works

1. Enter the Voter ID.
2. Upload a fingerprint image.
3. The fingerprint is preprocessed.
4. ORB features are extracted.
5. The fingerprint is compared with enrolled fingerprints.
6. If a match is found:
   - The registered Voter ID is displayed.
7. If no match is found:
   - The fingerprint is enrolled and linked with the entered Voter ID.

---

## Modules

### Image Preprocessing
Enhances the fingerprint image for better feature extraction.

### Feature Extraction
Extracts ORB descriptors from the fingerprint.

### Fingerprint Matching
Compares descriptors with stored templates to identify the best match.

### Database
Stores Voter IDs and fingerprint template references using SQLite.

---

## Future Improvements

- Fingerprint liveness detection
- Fingerprint quality assessment
- Faster matching using indexing
- Admin dashboard
- User authentication
- Cloud database integration
- Support for live fingerprint scanners

---

## Author

**Boda Karthikey Netha**

GitHub: https://github.com/karthikey-boda

---

## License

This project is developed for educational and academic purposes.
