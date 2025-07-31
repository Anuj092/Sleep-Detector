## 💤 Sleep Detector – Real-Time Drowsiness Monitoring

A Python application that monitors eye activity via webcam and detects signs of drowsiness using facial landmarks. Designed to alert users when eyes remain closed for extended periods — ideal for safety-critical applications like driver monitoring.

---

## Dataset
The dataset used for this project can be found [here](https://drive.google.com/drive/folders/1HNk3O4uMNWmE09DQYzfmYsLevW3oOPvT?usp=sharing).

---

## ⚙️ Tech Stack

- Python
- OpenCV
- Dlib (Facial Landmark Detection)
- NumPy
- Pygame (for alert sound)

---

## 🧠 How It Works

The system calculates the Eye Aspect Ratio (EAR) from key facial landmarks. If the ratio drops below a set threshold for consecutive frames, an alarm is triggered.

---

## 🎯 Features

- 🎥 Real-time webcam monitoring (30+ FPS)
- 👁️ Facial landmark tracking with Dlib
- 🚨 Alarm sound for prolonged eye closure
- 📊 Adjustable threshold and detection sensitivity
- 🪶 Lightweight (CPU-friendly)

---

## 📊 Performance Metrics

| Metric              | Value           |
|---------------------|-----------------|
| Video FPS           | ~30             |
| EAR Detection Latency | < 100ms        |
| Detection Accuracy  | 90%+ (in good light) |
| Alert Response Time | ~500ms          |

---

## 🛠 Setup Instructions

```bash
git clone https://github.com/Anuj092/Sleep-Detector
cd Sleep-Detector
pip install -r requirements.txt
python sleep_detector.py


---

<div align="center">
  <a href="#top">Back to top</a>
</div>

