

# 📏 Posture Detection Bot

A Python-based real-time posture detection tool that uses **MediaPipe** and **OpenCV** to analyze body alignment through your webcam. It provides instant visual feedback on whether you are sitting or standing upright to help you maintain good posture and avoid discomfort or long-term health issues.

---

## 🚀 Features
- **Real-time posture analysis**: Detects your posture instantly using webcam feed.
- **Visual feedback**: Displays posture status directly on the video:
  - 🟢 **Green**: You are upright.
  - 🔴 **Red**: You are slouching.
- Lightweight and easy to set up.

---

## 📋 How It Works
1. **Pose Estimation**: The tool leverages the **MediaPipe Pose** model to track key body landmarks such as shoulders and hips.
2. **Posture Evaluation**: It calculates the vertical alignment of the shoulders and hips to determine if the user is upright.
3. **Feedback**: Based on the analysis:
   - If the shoulders and hips are vertically aligned (within a certain threshold), it marks the posture as **upright**.
   - Otherwise, it marks the posture as **slouching**.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/maurux01/posture-detection-bot.git
   cd posture-detection-bot
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required libraries:
   ```bash
   pip install mediapipe opencv-python
   ```

3. **Run the Script**:
   ```bash
   python posture_detection_bot.py
   ```

---

## 🖥️ Usage Instructions

- **Webcam Activation**: Once the script is running, your webcam will activate automatically.
- **Posture Feedback**:
  - Sit or stand in front of the camera.
  - The bot will analyze your posture and display feedback in real-time.
- **Exit**: Press `q` to close the application.

---

## ⚙️ Configuration

You can adjust the detection sensitivity by modifying the **posture threshold** in the script. The default threshold is `0.05`, which you can increase or decrease for stricter or more lenient posture evaluation.

---

## 📷 Screenshots
*(Include screenshots here if available to showcase the tool in action.)*

---

## 🤔 Why Use This?

Good posture is essential for:
- Reducing back and neck pain.
- Improving focus and energy levels.
- Preventing long-term health complications like spinal misalignment.

This tool serves as a quick and practical way to monitor your posture and develop healthier habits.

---

## 👤 About the Creator

This project was developed by **maurux01**, an industrial engineer and programmer passionate about merging technology and wellness.  

Visit my GitHub: [maurux01](https://github.com/maurux01)

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share it. Contributions are welcome!

---

## 🤝 Contributions

If you’d like to enhance this project:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request with a brief description of the updates.

---

*Stay upright, stay healthy, and keep coding!*
```


