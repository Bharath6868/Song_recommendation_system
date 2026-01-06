# 🎶 Song Recommendation System

## 📌 Overview
This project is a **mood-based music recommendation application** built using **Streamlit** and the **Google Gemini API**.  
Users provide their current mood, and the system generates a curated list of songs along with artist names in a structured tabular format.

This project is designed as a **recruiter-facing demo** showcasing Generative AI integration, NLP preprocessing, and an interactive UI.

---

## 🎯 Key Objectives
- Demonstrate real-world **Generative AI** usage for recommendation systems  
- Build an interactive and deployable **Streamlit application**  
- Apply clean **NLP preprocessing** techniques  
- Maintain a simple, reproducible, and audit-friendly codebase  

---

## 🛠️ Tech Stack & Skills Demonstrated

| Category | Tools / Concepts |
|--------|----------------|
| Programming Language | Python |
| UI Framework | Streamlit |
| Generative AI | Google Gemini API |
| NLP Preprocessing | `lower()`, `strip()` |
| Environment Handling | `python-dotenv`, `.env` |
| API Integration | Secure key loading |
| Output Format | Tabular recommendations |

---

## 📂 Project Flow

### 1. Environment Setup
- Install required dependencies
- Load API key securely using `.env`

### 2. Gemini API Configuration
- Initialize Gemini client
- Handle API calls safely

### 3. UI Design
- Application title and markdown sections
- Input field for user mood
- Clean, recruiter-friendly layout

### 4. Input Normalization
- Convert text to lowercase
- Remove extra whitespace using `strip()`

### 5. Generative Recommendation
- Prompt Gemini model to recommend **5 songs**
- Include **song name and artist**
- Format output as a table

### 6. Output Rendering
- Display results clearly in Streamlit
- Show feedback if input is missing

---

## 🚀 How to Run

### Clone Repository
```bash
git clone https://github.com/yourusername/song-recommendation-system.git
cd song-recommendation-system
