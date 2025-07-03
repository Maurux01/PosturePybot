import cv2
import mediapipe as mp
import sys
import time
import threading
import platform

try:
    import winsound  # For Windows sound alert
except ImportError:
    winsound = None

# Configurable threshold for posture detection
POSTURE_THRESHOLD = 0.05  # Default value, can be changed

# Function to play a sound alert (cross-platform)
def play_alert():
    if platform.system() == "Windows" and winsound:
        winsound.Beep(1000, 500)  # frequency, duration
    else:
        # For Linux/Mac, try to use 'beep' or system bell
        print("\a")

# Function to calculate average y position of two landmarks
def avg_y(landmarks, idx1, idx2):
    return (landmarks[idx1].y + landmarks[idx2].y) / 2

# Main posture detection function
def run_posture_detection(threshold=POSTURE_THRESHOLD):
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        sys.exit(1)

    print("Posture detection started. Press 'q' to quit.")
    print(f"Current threshold: {threshold}")

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        good_posture_time = 0
        bad_posture_time = 0
        last_status = None
        start_time = time.time()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read from webcam.")
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            frame = cv2.flip(frame, 1)

            posture_status = "Unknown"
            color = (255, 255, 0)  # Default: yellow
            alert = False

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                landmarks = results.pose_landmarks.landmark
                shoulder_y = avg_y(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.RIGHT_SHOULDER)
                hip_y = avg_y(landmarks, mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.RIGHT_HIP)
                diff = abs(shoulder_y - hip_y)

                if diff < threshold:
                    posture_status = "You are upright"
                    color = (0, 255, 0)  # Green
                    if last_status != "good":
                        good_posture_time += 1
                        last_status = "good"
                else:
                    posture_status = "You are slouching!"
                    color = (0, 0, 255)  # Red
                    alert = True
                    if last_status != "bad":
                        bad_posture_time += 1
                        last_status = "bad"

            # Show posture status on screen
            cv2.putText(frame, posture_status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            cv2.putText(frame, "Press 'q' to quit", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 1)
            cv2.putText(frame, f"Threshold: {threshold}", (30, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 1)

            # Show statistics
            elapsed = int(time.time() - start_time)
            stats = f"Good: {good_posture_time}s  Bad: {bad_posture_time}s  Time: {elapsed}s"
            cv2.putText(frame, stats, (30, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 255, 255), 1)

            cv2.imshow('Posture Detection', frame)

            if alert:
                # Play alert sound in a separate thread to avoid blocking
                threading.Thread(target=play_alert, daemon=True).start()

            key = cv2.waitKey(10) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('+'):
                threshold = min(threshold + 0.01, 0.2)
            elif key == ord('-'):
                threshold = max(threshold - 0.01, 0.01)

    cap.release()
    cv2.destroyAllWindows()
    print("Session ended.")
    print(f"Total good posture time: {good_posture_time}s")
    print(f"Total bad posture time: {bad_posture_time}s")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Real-time posture detection using webcam and MediaPipe Pose.")
    parser.add_argument('--threshold', type=float, default=POSTURE_THRESHOLD, help='Threshold for posture detection (default: 0.05)')
    args = parser.parse_args()
    run_posture_detection(args.threshold)
