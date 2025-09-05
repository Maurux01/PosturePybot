# 🦾 Real-Time Posture Detection Bot

A Python bot that monitors your posture in real time using your webcam, powered by **MediaPipe** and **OpenCV**. It provides instant visual and sound feedback to help you maintain a healthy, upright posture while sitting or standing.


---

## 🚀 Features
- **Real-time posture analysis** using your webcam
- **Visual feedback**: On-screen status ("You are upright" or "You are slouching!") with color coding
- **Sound alert** when bad posture is detected
- **Live statistics**: Tracks time spent in good and bad posture
- **Configurable sensitivity threshold** (adjustable during runtime)
- **Cross-platform support** (Windows, Linux, Mac)

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Maurux01/PosturePybot
   cd PosturePybot
   ```

2. **Install Dependencies and Run (Windows)**
   You can use the provided batch script for easy setup:
   ```bat
   install_and_run.bat
   ```

3. **Install Dependencies and Run (Linux)**
   Use the provided shell script for easy setup:
   ```bash
   chmod +x install_and_run.sh
   ./install_and_run.sh
   ```

If you prefer manual installation, ensure you have Python 3.7+ and run:
```bash
pip install -r requirements.txt
python pybot.py
```

---

## 🖥️ Usage

Run the bot with the default threshold:
```bash
python pybot.py
```

Or specify a custom threshold (default is 0.05):
```bash
python pybot.py --threshold 0.07
```

### Controls
- **q**: Quit the application
- **+**: Increase sensitivity threshold (stricter)
- **-**: Decrease sensitivity threshold (more lenient)

---

## 📋 How It Works
1. **Pose Estimation**: Uses MediaPipe Pose to detect key body landmarks (shoulders, hips).
2. **Posture Evaluation**: Calculates the vertical difference between the average y-coordinates of the shoulders and hips.
3. **Feedback**:
   - If the difference is less than the threshold, you are considered upright (green message).
   - If the difference exceeds the threshold, you are slouching (red message + sound alert).
4. **Statistics**: Tracks and displays the time spent in good and bad posture during the session.

---

## ⚙️ Configuration
- **Threshold**: The sensitivity for posture detection. Lower values are stricter. You can set it at launch with `--threshold` or adjust it live with `+` and `-` keys.

---

## 🚦 Performance Tips
If you are running the bot on a low-resource system, consider the following tips to improve performance:
- **Close other applications** that may be using the webcam or consuming CPU/RAM.
- **Lower webcam resolution**: Edit the script to set a lower resolution for the video capture (e.g., 640x480).
- **Use 64-bit Python** for better memory management.
- **Run in a well-lit environment** to help MediaPipe detect landmarks more efficiently.
- **Keep your Python and dependencies updated** for the latest performance improvements.

---

## ❗ Troubleshooting
- If you see an error about the webcam, ensure no other application is using it and that your device has a camera.
- For sound alerts on Linux/Mac, the system bell is used. On Windows, a beep is played.
- If you have issues with dependencies, ensure you are using a compatible Python version and that `opencv-python` and `mediapipe` are installed.

---

## 👤 Author
Developed by [maurux01](https://github.com/maurux01). Contributions and suggestions are welcome!

---

## 📜 License
MIT License. Feel free to use, modify, and share.

---

*Sit up straight, stay healthy, and keep coding!*
```
