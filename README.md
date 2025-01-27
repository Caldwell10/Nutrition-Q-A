# Nutrition Q&A System

A web-based Q&A system that allows users to query nutritional information using **Hugging Face**, **FAISS**, and **Flask**. The system leverages pre-trained NLP models to process queries and retrieve relevant results efficiently.

---

## Features

- Query nutritional information using natural language.
- Results ranked by relevance with FAISS similarity search.
- Filter results for high protein, low fat, or low calories.
- Deployed as a live web application for easy access.

---

## Tech Stack

1. **Backend**:
   - **Flask**: Lightweight Python framework for serving the web app.
   - **FAISS**: High-performance library for similarity search.
   - **Sentence Transformers**: Hugging Face pre-trained model for text embeddings.

2. **Frontend**:
   - HTML5, CSS3
   - Bootstrap for responsive design.

3. **Deployment**:
   - Deployed on **Render** for a live demo.

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Caldwell10/Nutrition-Q-A.git
   cd Nutrition-QA-System
   
2.Run the application:
```bash
python app.py
```
3. Open the app in your browser at http://127.0.0.1:5000/
