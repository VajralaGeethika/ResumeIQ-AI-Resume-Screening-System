# ResumeIQ – AI Resume Screening & ATS Scoring System

## Overview

ResumeIQ is an AI-powered Resume Screening and ATS Scoring System that automates resume analysis using Machine Learning and Natural Language Processing (NLP).

The application classifies resumes into job categories, calculates an ATS score based on role-specific skills, compares resumes against a Job Description, generates resume improvement suggestions, and provides a recruiter dashboard for ranking multiple candidates.


## Live Demo

https://resumeiq-ai-resume-screening-system.onrender.com

## Features
Resume Classification
ATS Score Calculation
Job Description Matching
Resume Improvement Suggestions
Recruiter Dashboard
Candidate Ranking

### Candidate Module

- Upload Resume (PDF/DOCX)
- Resume Category Prediction
- Confidence Score
- ATS Score Calculation
- Job Description Matching
- Matched Skills
- Missing Skills
- AI Resume Improvement Suggestions
- Resume Preview

### Recruiter Module

- Upload Multiple Resumes
- Automatic Candidate Ranking
- ATS Score Dashboard
- Candidate Statistics
- Interactive ATS Score Chart
- Resume Category Comparison


## Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- NLP
- Cosine Similarity

### Data Processing
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3
- Chart.js

### File Processing
- pdfplumber
- python-docx

## Project Structure

text
ResumeIQ-AI-Resume-Screening-System/

├── app/
│   ├── routes.py
│   ├── services.py
│   ├── static/
│   ├── templates/
│   ├── uploads/
│   └── utils/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── models/
│
├── notebooks/
├── requirements.txt
├── app.py
└── README.md


## Installation

Clone the repository

git clone https://github.com/VajralaGeethika/ResumeIQ-AI-Resume-Screening-System.git


## Workflow

1. Upload Resume
2. Extract Resume Text
3. Clean Resume
4. Predict Resume Category
5. Calculate ATS Score
6. Compare with Job Description
7. Generate Suggestions
8. Display Results
9. Recruiter Dashboard for Candidate Ranking


## Future Enhancements

- User Authentication
- Resume Parsing with OCR
- AI Chatbot for Resume Review
- Resume Keyword Optimization
- Email Notification System
- Cloud Deployment
- Export Reports as PDF
- Recruiter Login Portal

## Author

**Vajrala Geethika**

GitHub: https://github.com/VajralaGeethika


## License

This project is created for educational and portfolio purposes.
