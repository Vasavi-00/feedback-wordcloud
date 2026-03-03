# ☁️ Live Feedback Word Cloud

A simple web application that collects anonymous responses from users and visualizes them as a live word cloud.

Built using Python and Streamlit.

---

## 🚀 Features

- Collects anonymous feedback from users
- Generates a live word cloud visualization
- Automatically updates when new responses are submitted
- Removes common stopwords
- Allows downloading collected responses
- Simple and clean user interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- WordCloud
- Matplotlib

---

## 📂 Project Structure

feedback-wordcloud

app.py – Main Streamlit application  
requirements.txt – Required Python libraries  
README.md – Project documentation  
.gitignore – Files ignored by Git

---

## ⚙️ Installation (Run Locally)

1. Clone the repository

git clone https://github.com/Vasavi-00/feedback-wordcloud.git

2. Navigate into the folder

cd feedback-wordcloud

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

The app will start locally at:

http://localhost:8501

---

## 🌐 Deployment

This project can be deployed easily using Streamlit Cloud.

Steps:

1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Login with your GitHub account
4. Click "New App"
5. Select your repository
6. Choose app.py as the main file
7. Deploy

---

## 🔒 Privacy

This application does NOT collect any personal data.

Only the text responses entered by users are stored.

No names, emails, or IP addresses are recorded.

---

## 📊 Example Use Cases

- Workshop feedback
- Classroom participation
- Event audience interaction
- Opinion polling

---

## ❤️ Built With

Streamlit  
WordCloud  
Pandas  
Matplotlib