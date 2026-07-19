import cv2
from recognize import recognize_face

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    frame = recognize_face(frame)

    cv2.imshow("Recognition Test", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()