import cv2
import mediapipe as mp

# Inicializar MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Configuración de la cámara
cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir la imagen a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        # Dibujar las poses en la imagen
        frame = cv2.flip(frame, 1)  # Espejo para mayor comodidad
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extraer puntos clave
            landmarks = results.pose_landmarks.landmark

            # Puntos de interés para determinar postura
            shoulder_y = (landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y + 
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y) / 2
            hip_y = (landmarks[mp_pose.PoseLandmark.LEFT_HIP].y + 
                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y) / 2

            # Calcular diferencia entre hombros y cadera (si está recto o no)
            if abs(shoulder_y - hip_y) < 0.05:  # Umbral ajustable
                posture_status = "Estás erguido"
                color = (0, 255, 0)  # Verde
            else:
                posture_status = "Estás inclinado"
                color = (0, 0, 255)  # Rojo

            # Mostrar mensaje en la pantalla
            cv2.putText(frame, posture_status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # Mostrar la imagen en tiempo real
        cv2.imshow('Detección de postura', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
