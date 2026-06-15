# 🏥 Healthcare Assistant Chatbot

## 📌 Overview

The **Healthcare Assistant Chatbot** is an AI-powered healthcare information system developed using **Python**, **Streamlit**, and **Natural Language Processing (NLP)**. The chatbot provides users with general health information regarding common health topics such as fever, cold, headache, diet, exercise, first aid, and stress management.

The system uses keyword-based intent recognition and NLP techniques to understand user queries and provide relevant healthcare guidance while maintaining medical safety standards.

---

## 🚀 Features

* ✅ Interactive Chat Interface
* ✅ Natural Language Processing (NLP)
* ✅ Health Information Assistance
* ✅ Emergency Situation Detection
* ✅ Medication Safety Alerts
* ✅ Medical Diagnosis Safety Warnings
* ✅ Keyword-Based Intent Recognition
* ✅ Session-Based Chat History
* ✅ User-Friendly Streamlit Interface
* ✅ Fast Response Time

---

## 🛠️ Technologies Used

| Technology                  | Purpose                     |
| --------------------------- | --------------------------- |
| Python                      | Programming Language        |
| Streamlit                   | Web Application Framework   |
| NLTK                        | Natural Language Processing |
| Regular Expressions (Regex) | Text Cleaning               |
| WordNet Lemmatizer          | Word Normalization          |
| Tokenization                | Text Processing             |
| Session State               | Chat History Management     |

---

## 🏗️ System Architecture

```text
User Query
    │
    ▼
Text Preprocessing
    │
    ├── Lowercase Conversion
    ├── Tokenization
    ├── Stopword Removal
    └── Lemmatization
    │
    ▼
Keyword Extraction
    │
    ▼
Intent Recognition
    │
    ├── Emergency Detection
    ├── Diagnosis Request Detection
    ├── Medication Request Detection
    └── General Health Topic Detection
    │
    ▼
Response Generation
    │
    ▼
Healthcare Information
```

---

## 🤖 Functional Modules

### 1. NLP Processing Module

The chatbot processes user input through:

* Text Cleaning
* Tokenization
* Stopword Removal
* Lemmatization
* Keyword Extraction

This helps improve query understanding and matching accuracy.

---

### 2. Emergency Detection Module

The chatbot checks for emergency-related keywords such as:

* Chest pain
* Severe bleeding
* Difficulty breathing
* Heart attack symptoms

If detected, it immediately advises contacting emergency medical services.

---

### 3. Diagnosis Safety Module

If users ask for medical diagnosis, the chatbot responds with:

> "Please consult a qualified healthcare provider for personal medical concerns."

This prevents unsafe medical recommendations.

---

### 4. Medication Safety Module

The chatbot avoids prescribing medications and instead advises users to consult:

* Doctors
* Pharmacists
* Healthcare Professionals

---

### 5. Health Knowledge Base

The chatbot provides information on:

#### 🩺 Common Illnesses

* Fever
* Cold
* Flu
* Headache

#### 🥗 Nutrition

* Healthy Diet
* Balanced Nutrition
* Hydration

#### 🏃 Fitness

* Exercise
* Physical Activity
* Wellness

#### 🩹 First Aid

* Minor Injuries
* Basic Emergency Care

#### 🧘 Mental Health

* Stress Management
* Relaxation Techniques
* Healthy Lifestyle Habits

---

## 📂 Project Structure

```text
Healthcare-Assistant/
│
├── app.py
├── intents.py
├── requirements.txt
├── README.md
│
└── assets/
    ├── screenshots/
    └── icons/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/healthcare-assistant-chatbot.git

cd healthcare-assistant-chatbot
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📋 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
nltk
```

Install manually:

```bash
pip install streamlit nltk
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running, the application will open automatically in your browser.

---

## 🧠 NLP Techniques Used

### Tokenization

Breaks user input into smaller words (tokens).

Example:

```text
Input:
"I have a severe headache"

Output:
["I", "have", "a", "severe", "headache"]
```

---

### Stopword Removal

Removes unnecessary words:

```text
have
a
the
is
are
```

---

### Lemmatization

Converts words to their root form.

Example:

```text
running → run
exercises → exercise
```

---

### Intent Matching

Matches extracted keywords against predefined healthcare topics.

Example:

```text
headache
migraine
pain
```

→ Headache Intent

---

## 📊 Example Queries

### Fever

```text
What should I do if I have a fever?
```

### Cold & Flu

```text
How can I recover from a cold?
```

### Diet

```text
What is a balanced diet?
```

### Exercise

```text
How much exercise should I do daily?
```

### Stress Management

```text
How can I reduce stress naturally?
```

---

## 🔒 Safety Features

### Emergency Alerts

Detects potentially dangerous symptoms and advises emergency assistance.

### Diagnosis Prevention

Prevents AI-generated medical diagnoses.

### Medication Safety

Avoids providing medication prescriptions.

### Healthcare Disclaimer

Clearly states that information is educational and not medical advice.

---

## 🎯 Future Enhancements

* Integration with Large Language Models (LLMs)
* Voice-Based Healthcare Assistant
* Symptom Tracking Dashboard
* Appointment Scheduling System
* Medical Report Analysis
* Multi-Language Support
* Health Risk Prediction
* Personalized Wellness Recommendations

---

## 📸 Screenshots

### Home Page

(Add Screenshot Here)

### Chat Interface

(Add Screenshot Here)

### Emergency Alert Example

(Add Screenshot Here)

---

## 👨‍💻 Author

**Swaraj Nikam**

B.Tech Student
AI & Data Science Enthusiast

Areas of Interest:

* Artificial Intelligence
* Healthcare Technology
* Natural Language Processing
* Machine Learning
* Data Analytics

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

* Star ⭐ the repository
* Fork 🍴 the project
* Contribute 🚀 improvements
* Share 📢 with others

---

## 🏆 Conclusion

The Healthcare Assistant Chatbot demonstrates the practical application of Natural Language Processing in healthcare information systems. By combining NLP techniques with safety-focused design, the chatbot delivers reliable health information while encouraging users to seek professional medical advice when necessary.
