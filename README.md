# 🩺 Medical Q&A Chatbot using MedQuAD Dataset

## 📌 Description

This project is a specialized **Medical Question-Answering Chatbot** built using the **MedQuAD dataset** provided by the U.S. National Library of Medicine (NLM). The chatbot uses semantic search to retrieve the most relevant answers from a trusted medical dataset and recognizes medical entities like diseases, symptoms, and treatments.

It is designed to assist users by answering their medical questions using real and verified data.

---

## ⚙️ Features

- ✅ Processes 5000+ medical question-answer pairs from XML data
- ✅ Uses **Sentence Transformers** for accurate semantic matching
- ✅ Performs **Medical Entity Recognition (NER)** with `SciSpacy`
- ✅ Simple and clean **Streamlit UI**
- ✅ Built using Python and fully open-source

---

## 🛠️ Technologies Used

- Python 3.10
- Streamlit
- Pandas, NumPy
- Sentence-Transformers
- Spacy + SciSpacy (with `en_core_sci_sm` model)
- MedQuAD Dataset (converted to `qa_data.csv`)

---

## 📁 Files Included

| File Name            | Description                             |
|----------------------|-----------------------------------------|
| `UI.py`              | Main Streamlit app code (chatbot logic) |
| `medical_chatbot.ipynb` | Jupyter Notebook version of development |
| `qa_data.csv`        | Final processed dataset used for Q&A    |
| `requirements.txt`   | Python dependencies                     |

---

---

## 🧪 Setup & Installation Guide

Follow the steps below to run the chatbot locally on your machine:

### 🔹STEP 1. Create & Activate Virtual Environment (Recommended)

Use **Anaconda Prompt** on Windows:

```bash
conda create -n medqa python=3.10
conda activate medqa

🐍 STEP 2: Create & Activate Virtual Environment (optional but recommended)
Using Anaconda Prompt (Windows recommended):
  conda create -n medqa python=3.10
  conda activate medqa

📦 STEP 3: Install Required Packages:
   pip install -r requirements.txt

📂 STEP 4: Make Sure the qa_data.csv File Exists:
  Ensure that qa_data.csv is present in the same folder where your UI.py file is.
  If not, download it from repository.

▶️ STEP 5: Run the Streamlit App
In Anaconda Prompt (in the same directory as UI.py):
  streamlit run UI.py
  #This will open a browser window with the chatbot interface.


🛠️ How to Run the Medical Q&A Chatbot:
# Step 1: Clone the repository
git clone https://github.com/PrasadPardeshi20/medical-question-answering-chatbot.git

# Step 2: Navigate to the project directory
cd medical-question-answering-chatbot

# Step 3: Install the dependencies
pip install -r Requirments.txt

# Step 4: Run the chatbot
streamlit run UI.py


✨ Example Usage
You can ask questions like:
  1) What is leukemia?
  2)How is diabetes treated?
  3)What are symptoms of asthma?

🙌 Credits
  Dataset: MedQuAD - NLM/NIH
  Developed as part of a Data Science Internship Task

## ScreenShot :
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/68016e1d-44f7-48d9-a71b-2dff1f9769e4" />
