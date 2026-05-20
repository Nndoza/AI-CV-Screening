# AI CV Screening System

## Project Overview

This is a Flask-based AI CV Screening application that allows users to upload PDF CVs and automatically extract text and detect technical skills from the uploaded document.

The project was built as part of a cloud and DevOps learning journey focused on backend development, Linux, Git, GitHub, and AWS architecture concepts.

---

## Features

- Upload PDF CVs
- Extract text from uploaded CVs
- Detect predefined technical skills
- Display CV match score
- Flask backend application
- Git and GitHub version control

---

## Technologies Used

- Python
- Flask
- PyPDF2
- HTML
- CSS
- Linux
- Git
- GitHub

---

## Project Structure

```bash
ai-cv-screening/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── uploads/
│
└── venv/
```

---

## How To Run The Project

### 1. Clone Repository

```bash
git clone https://github.com/Nndoza/AI-CV-Screening.git
```

### 2. Navigate Into Project

```bash
cd AI-CV-Screening
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Flask Application

```bash
python app.py
```

---

## Future Improvements

- Deploy application on AWS EC2
- Store uploaded CVs in Amazon S3
- Use DynamoDB for candidate data
- Add authentication system
- Add AI/ML keyword ranking
- Dockerize the application
- Create CI/CD pipeline

---

## Learning Outcomes

This project helped strengthen my understanding of:

- Linux terminal commands
- Python backend development
- Flask applications
- File handling
- Git and GitHub workflows
- Debugging and troubleshooting
- Cloud architecture planning