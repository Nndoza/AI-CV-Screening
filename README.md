# AI CV Screening System

## Overview

This project focuses on building an AI-powered CV screening system using Python and Flask. The application allows recruiters or hiring teams to upload CVs in PDF format, extract candidate information, detect technical skills, and calculate a CV match score based on predefined skills.

The project was built as part of my cloud, backend, and DevOps learning journey to strengthen my understanding of Linux, Git, GitHub, Python backend development, and AWS architecture concepts.

---

## Problem Statement

Recruitment companies and HR teams often receive thousands of CV applications every week for different job roles. Manually reviewing each CV becomes time-consuming, repetitive, and inefficient, especially when recruiters need to quickly identify candidates with specific technical skills.

This creates challenges such as:

* Long screening times
* Human error during filtering
* Delays in shortlisting candidates
* Difficulty handling large application volumes

---

## Client Requirement

The goal was to build a simple web-based system that can:

* Allow recruiters to upload candidate CVs
* Extract text automatically from PDF documents
* Detect technical skills from the uploaded CV
* Calculate a simple CV match score
* Display results in a clean and user-friendly interface

The system should also be lightweight, scalable, and easy to improve in the future using cloud services and automation tools.

---

## Solution Overview

To solve this problem, I built a Flask web application that processes uploaded PDF CVs and scans them for predefined technical skills such as AWS, Python, Linux, Docker, Terraform, Git, Flask, and CI/CD.

Once the CV is uploaded:

1. The application extracts text from the PDF using PyPDF2
2. The extracted text is scanned against a predefined skills list
3. Matching skills are detected automatically
4. A CV match score is calculated
5. Results are displayed directly on the web interface

The project demonstrates how backend systems can automate repetitive recruitment tasks and improve screening efficiency.

---

## Features

* Upload PDF CVs
* Extract text from PDF documents
* Detect technical skills automatically
* Calculate CV match score
* Display extracted CV content
* User-friendly Flask web interface
* Git and GitHub version control integration

---

## Technologies Used

* Python
* Flask
* PyPDF2
* HTML
* CSS
* Linux
* Git
* GitHub

---

## Technical Approach

### Backend Development

The backend application was built using Flask. The application handles file uploads, processes PDF files, extracts text, and performs skill matching logic.

### Skill Detection

A predefined Python list was created containing technical skills. The application loops through the extracted text and compares it against the skills list to identify matches.

### CV Match Score

The project calculates a simple percentage score based on how many predefined skills were detected in the uploaded CV.

### Version Control

Git and GitHub were used to manage project versions, commits, and repository hosting.

---

## How To Run The Project

### 1. Clone The Repository

```bash
git clone https://github.com/Nndoza/AI-CV-Screening.git
```

### 2. Navigate Into The Project Folder

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

### 5. Install Project Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run The Flask Application

```bash
python app.py
```

### 7. Open The Application In Browser

```text
http://127.0.0.1:5000
```

---

## Challenges & Debugging

One of the biggest lessons during this project was learning how important debugging and troubleshooting are in backend development.

Some challenges I faced included:

* GitHub authentication errors caused by password authentication deprecation
* Understanding the difference between tracked and untracked Git files
* Learning how Git staging, commits, and pushes work together
* Debugging Flask errors such as variable scope issues

Working through these problems helped me better understand developer workflows and strengthened my confidence using Linux, Git, GitHub, and Flask.

---

## Future Improvements

Some future improvements I would like to implement include:

* Deploying the application on AWS EC2
* Storing uploaded CVs in Amazon S3
* Using DynamoDB for candidate storage
* Adding authentication and recruiter login
* Building a more advanced AI ranking system
* Dockerizing the application
* Creating a CI/CD pipeline for automated deployments

---

## Conclusion

This project helped me gain practical experience in backend development, Linux workflows, Git version control, debugging, and cloud architecture thinking.

Although CV screening systems already exist in the real world, this project was built to demonstrate my ability to design and build a working solution that solves a real business problem using modern development tools and cloud-focused concepts.
