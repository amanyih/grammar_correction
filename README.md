---
title: Grammar Correction
emoji: 🦀
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.41.1
app_file: app.py
pinned: false
license: mit
short_description: Grammar Correction for NLP course
---

---

**NLP Project**

This repository contains a Grammar Correction tool developed as part of the NLP project by **Software Group 2**. The tool leverages NLP techniques to detect and correct grammatical mistakes in user-provided text. It is designed to be user-friendly and provides two options for running the application: a Streamlit-based interactive app or a traditional web-based app.

---

## **Team Members**

- **AMANUEL YIHUNE HIBSTE** - UGR/8408/13
- **ARYAM WUBSHET BERHANU** - UGR/6357/13
- **BASLIEL AMSALU GELETU** - UGR/8569/13
- **BEREKET LEGESSE TADESSE** - UGR/7987/13
- **BETSELOT KIDANE BONSA** - UGR/8473/13

---

## **How to Run Locally**

### **Step 1: Clone the Repository**

```bash
git clone
cd repo
```

### **Step 2: Create a Virtual Environment**

Create a virtual environment to manage dependencies:

```bash
python -m venv env
.\env\Scripts\activate
```

### **Step 3: Install Requirements**

Install all necessary dependencies:

```bash
pip install -r requirements.txt
```

### **Step 4: Train the Model**

Run the training script to prepare the model:

```bash
python model.py
```

### **Step 5: Run the App**

#### **Option 1: Run as a Traditional Web App**

To run the app locally and access it via an HTML page:

```bash
python app_flask.py
```

#### **Option 2: Run as a Streamlit App**

For an interactive Streamlit-based application:

```bash
streamlit run app.py
```

---

## **Features**

- Grammar error detection and correction
