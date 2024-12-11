# Email Scam Detector

This project is an email scam detector application that uses a pre-trained Transformer model to classify email content as scam or legitimate. The application consists of a Flask backend and a simple HTML-based frontend, allowing users to paste email content for real-time analysis.

---

## **Libraries and Installation Instructions**

To set up the project locally, you need to install the following Python libraries:

### **1. Flask**
**Purpose**: Flask is used to create the backend web server for the application. It handles incoming requests from the frontend and returns classification results.
- **Installation**:
  ```bash
  pip install flask

### **2. Flask-CORS**
**Purpose**: Enables Cross-Origin Resource Sharing (CORS) so that the frontend can communicate with the Flask backend without being blocked by the browser’s security policies.
- **Installation**:
  ```bash
  pip install flask-cors

### **3. Transformers**
**Purpose**: Hugging Face's transformers library provides access to pre-trained state-of-the-art models for natural language processing. The application uses the distilbert-base-uncased model for text classification.
Why We Use It:
It can analyze complex language patterns in email content.
It provides pre-trained models, saving time and computational resources.
- **Installation**:
  ```bash
  pip install transformers

### **4. Torch**
**Purpose**: torch is the deep learning framework required to run Transformer models. It serves as the backend for model computations.
- **Installation**:
  ```bash
  pip install torch

## How to Set Up the Project
Follow these steps to run the project locally:

1. Clone the Repository
bash
Copy code
git clone <your-repository-url>
cd <repository-folder>
2. Install Dependencies
Install the required Python libraries:

bash
Copy code
pip install flask flask-cors transformers torch
3. Start the Backend
Run the Flask server:

bash
Copy code
python server.py
The backend will start at http://localhost:4000.

4. Serve the Frontend
Use Python's built-in HTTP server to serve the index.html file:

bash
Copy code
python -m http.server 8000
Open your browser and navigate to http://localhost:8000.
