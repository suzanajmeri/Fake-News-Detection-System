# 📰 Fake News Detection System

Fake News Detection System is a Machine Learning and Natural Language Processing (NLP) based web application that predicts whether a news article is Real or Fake. This project was created to understand the impact of misinformation and show how Artificial Intelligence can help solve real-world problems.

The system analyzes user news content using TF-IDF Vectorization and predicts authenticity using a trained Logistic Regression model. The application also provides a modern and interactive interface built with Streamlit.

This project improved my practical knowledge of Machine Learning, NLP, Python development, and AI-based application building.

## 🚀 Features

✅ Fake & Real News Prediction  
✅ Interactive Streamlit Interface  
✅ NLP Text Processing  
✅ Machine Learning Integration  
✅ Category-wise News Analysis  
✅ Fast & User-Friendly System  
✅ Modern UI Design  

## 🛠️ Technologies Used

- Python
- Streamlit
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- Pandas
- NumPy
- Pickle

## 🧠 Machine Learning Concepts Used

- Text Cleaning
- TF-IDF Vectorization
- Logistic Regression
- Text Classification
- Train-Test Split
- Model Serialization

## 📂 Project Structure

```bash
Fake-News-Detection/
│
├── interface.py
├── train.py
├── fake.csv
├── authentic.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/fake-news-detection.git
```

### 2️⃣ Open Project Folder

```bash
cd fake-news-detection
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 4️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 5️⃣ Train the Model

```bash
python train.py
```

This will generate:

- model.pkl
- vectorizer.pkl

### 6️⃣ Run the Application

```bash
streamlit run interface.py
```

## 🌐 Open in Browser

```bash
http://localhost:8501
```

## 📊 Project Workflow

1. Load Fake & Real News Dataset  
2. Clean and preprocess text data  
3. Convert text into vectors using TF-IDF  
4. Train Logistic Regression model  
5. Save model and vectorizer  
6. Build Streamlit web interface  
7. Predict whether news is Fake or Real  

## 🖥️ Application Pages

### 🏠 Home Page
Users can paste any news article and instantly check whether it is Fake or Real.

### 📂 Category Page
Includes sample headlines from:
- Politics
- Sports
- Technology
- Health
- Entertainment

### ℹ️ About Page
Displays project details, features, and developer information.

## 📸 Prediction Output

### ✅ Real News
The article appears authentic and trustworthy.

### ❌ Fake News
The article appears misleading or fake.

## 🎯 Project Objective

- Reduce misinformation spread
- Create awareness about fake news
- Learn practical implementation of NLP and Machine Learning
- Build a real-world AI application

## 🔮 Future Improvements

- Add Live News API Integration
- Improve Accuracy using Deep Learning
- Add Multi-language Support
- Deploy Project Online
- Add User Authentication System

## 📚 Learning Outcomes

- Machine Learning Fundamentals
- NLP Text Processing
- Streamlit Application Development
- Model Training & Prediction
- Real-world AI Project Development

## 👨‍💻 Developer

**Suzan Ajmeri**  
BCA Student | Python Developer | Machine Learning Enthusiast

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.

## 📌 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
```

## ▶️ Run Command

```bash
streamlit run interface.py
```
