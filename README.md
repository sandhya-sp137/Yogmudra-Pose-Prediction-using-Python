# 🧘‍♀️ Yog Mudra Pose Prediction Using Python

> **AI-powered Yoga Pose Recognition using Computer Vision, MediaPipe, Machine Learning and Streamlit**

## 📌 Overview

**Yog Mudra Pose Prediction** is a Python-based computer vision and machine learning project that identifies yoga poses from input images and provides useful information about the predicted pose.

The system combines **MediaPipe-based human pose estimation**, **CNN-based pose classification**, **cosine similarity for pose comparison**, a **Streamlit web interface**, a **CSV-based pose information database**, and **YouTube Data API integration**.

The application is designed as a lightweight virtual yoga assistant that can help users understand yoga poses, their steps, benefits, precautions and related tutorial videos.

The project was developed as a B.Tech Artificial Intelligence & Data Science project at **Fabtech Technical Campus, College of Engineering & Research, Sangola**, under Dr. Babasaheb Ambedkar Technological University, Lonere, during the academic year 2024–2025.

---

## ✨ Key Features

- 📷 Upload an image of a yoga pose
- 🤖 Predict the yoga pose using a trained ML/DL model
- 🦴 Detect human body landmarks using MediaPipe
- 📊 Generate a prediction/confidence score
- 📐 Compare detected pose keypoints using cosine similarity
- 📚 Display pose name, steps, benefits and precautions
- 🎥 Fetch related yoga tutorial videos using YouTube Data API
- 🔎 Search for a yoga pose by name
- 🌐 Simple and interactive Streamlit web interface
- 💻 Runs on a standard computer without expensive hardware

---

## 🏗️ System Workflow

```text
                 ┌─────────────────────┐
                 │     User Input      │
                 │   Image / Pose      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Image Preprocessing │
                 │      OpenCV         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Pose Estimation    │
                 │     MediaPipe       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Body Keypoints /   │
                 │   Feature Vector    │
                 └──────────┬──────────┘
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ CNN Classifier  │   │ Cosine Similarity│
        │ Pose Prediction │   │ Pose Comparison │
        └────────┬────────┘   └────────┬────────┘
                 │                     │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │   Pose Information  │
                 │       CSV           │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   YouTube Data API  │
                 │  Tutorial Retrieval │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Streamlit Output  │
                 │ Pose + Score + Info  │
                 │ + Tutorial Video    │
                 └─────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Image processing |
| MediaPipe | Human pose/keypoint detection |
| TensorFlow | Deep learning/model execution |
| Keras | CNN model development |
| NumPy | Numerical operations |
| Pandas | CSV/data handling |
| Streamlit | Web application interface |
| YouTube Data API | Yoga tutorial video retrieval |
| CSV | Pose information storage |
| Git/GitHub | Version control |

---

## 🧠 How the System Works

### 1. Image Input

The user uploads an image containing a yoga pose through the Streamlit interface.

### 2. Image Preprocessing

OpenCV is used to read, resize/normalize and prepare the input image for pose analysis.

### 3. Pose Detection

MediaPipe detects human body landmarks/keypoints from the image.

The extracted points are converted into a structured feature vector.

Example:

```text
X1, Y1, X2, Y2, X3, Y3, ... , Xn, Yn
```

### 4. Pose Classification

The processed features are passed to the trained classification model to predict the yoga pose and its confidence score.

### 5. Pose Similarity

Cosine similarity can be used to compare the user's extracted pose vector with stored reference pose vectors.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(
    user_pose_vector,
    reference_pose_vector
)

print("Pose Similarity:", similarity)
```

### 6. Pose Information

After prediction, the application searches the CSV database for information related to the predicted pose.

Example information:

```text
Pose Name
Steps
Benefits
Precautions
```

### 7. YouTube Tutorial

The predicted pose name is used as a search query with the YouTube Data API to retrieve a relevant tutorial.

---

## 📂 Recommended Project Structure

```text
Yog-Mudra-Pose-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── yoga_pose_model.h5
│   └── reference_keypoints/
│
├── dataset/
│   ├── train/
│   └── test/
│
├── data/
│   └── yoga_poses.csv
│
├── static/
│   └── images/
│
└── utils/
    ├── pose_detection.py
    ├── prediction.py
    └── youtube_api.py
```

> **Note:** Rename files/folders in this structure to match the exact files present in your GitHub repository.

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the main libraries:

```bash
pip install opencv-python mediapipe tensorflow keras numpy pandas streamlit scikit-learn google-api-python-client
```

---

# 🔑 YouTube API Configuration

The project uses the **YouTube Data API** to retrieve yoga tutorial videos.

Create a Google API key and store it as an environment variable.

### Windows PowerShell

```powershell
$env:YOUTUBE_API_KEY="YOUR_API_KEY"
```

### macOS / Linux

```bash
export YOUTUBE_API_KEY="YOUR_API_KEY"
```

Or use a `.env` file if your implementation supports environment variables:

```env
YOUTUBE_API_KEY=YOUR_API_KEY
```

### ⚠️ Important

Never upload your real API key to GitHub.

Add this to `.gitignore`:

```gitignore
.env
*.key
secrets/
```

---

# ▶️ Run the Application

If your main Streamlit file is `app.py`:

```bash
streamlit run app.py
```

Then open the local URL shown by Streamlit, usually:

```text
http://localhost:8501
```

---

# 📊 Example Prediction Flow

```text
Upload Yoga Image
       ↓
OpenCV Preprocessing
       ↓
MediaPipe Keypoint Detection
       ↓
Feature Extraction
       ↓
CNN Pose Classification
       ↓
Cosine Similarity Check
       ↓
Pose Information from CSV
       ↓
YouTube Tutorial Search
       ↓
Display Final Result
```

---

# 📈 Results

According to the project evaluation, sample pose similarity values were:

| Input | Similarity |
|---|---:|
| File 1 | 80% |
| File 2 | 76% |
| File 3 | 94% |

Sample pose prediction accuracy:

| Input | Accuracy |
|---|---:|
| File 1 | 86% |
| File 2 | 89% |
| File 3 | 91% |

The reported processing times for sample poses were:

| Pose | Processing Time |
|---|---:|
| Bhujangasana | 145 ms |
| Vrikshasana | 130 ms |
| Trikonasana | 160 ms |
| Tadasana | 140 ms |
| Sarvangasana | 150 ms |

The report also compares the proposed feedback/similarity-based approach with a baseline system using precision and recall measurements.

---

# 🎯 Project Objectives

- Detect and classify yoga poses from images.
- Study human pose estimation using computer vision.
- Extract body keypoints for pose analysis.
- Build a machine learning/deep learning-based pose classifier.
- Provide confidence/similarity information.
- Display pose instructions, benefits and precautions.
- Integrate YouTube tutorials for visual learning.
- Build an easy-to-use web interface using Streamlit.
- Create a low-cost and accessible yoga learning assistant.

---

# 💡 Advantages

- Easy-to-use interface
- Uses open-source technologies
- No expensive specialized hardware required
- Combines AI with computer vision
- Provides educational pose information
- Supports video-based learning
- Can be extended to real-time pose correction
- Suitable for academic/research demonstrations

---

# ⚠️ Current Limitations

- The current version has limited pose coverage.
- Pose detection can be affected by image quality, visibility and body position.
- The system does not provide complete professional-level pose correction.
- YouTube tutorial retrieval requires internet access and API configuration.
- The project is primarily designed around image-based prediction in its documented implementation.

---

# 🔮 Future Scope

Possible future improvements include:

- 🎥 Real-time webcam pose detection
- 🔊 Voice-based yoga guidance
- 🧍 Real-time posture correction
- 📱 Android/mobile application
- 🌐 ReactJS frontend with Python backend
- 🗄️ MySQL/SQLite/Firebase database
- 👤 User profiles and practice history
- 📊 Progress tracking dashboard
- 🌍 Multilingual support
- 🤖 More advanced AI-based personalized feedback

---

# 🧪 Testing

The project includes testing of:

```text
Input Image
    ↓
Preprocessing
    ↓
Pose Detection
    ↓
Pose Classification
    ↓
Similarity Calculation
    ↓
Information Retrieval
    ↓
Final Output
```

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Pose similarity
- Processing time per frame

---

# 💻 Hardware Requirements

Minimum requirements described in the project report:

```text
Processor : Intel i3 or equivalent
RAM       : 8 GB
Storage   : ~1 GB free space
GPU       : Optional, useful for faster model training
```

---

# 📜 License

This project was developed as an academic/educational project.

You may add your preferred open-source license here, such as MIT License, after confirming the licensing requirements of the datasets, models and APIs used.

---

# 👩‍💻 Project Team

**B.Tech – Artificial Intelligence & Data Science**

- Sandhya Subhash Potadar
- Sanika Mahadev Pujari
- Shraddha Mukund Botre
- Neha Mahesh Suryavanshi

**Project Guide:** Prof. V. M. Sale

**Institution:** Fabtech Technical Campus, College of Engineering & Research, Sangola

**University:** Dr. Babasaheb Ambedkar Technological University, Lonere

**Academic Year:** 2024–2025

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub and feel free to explore the code.

```text
AI + Computer Vision + Yoga = Smart Yoga Assistant 🧘‍♀️🤖
```
