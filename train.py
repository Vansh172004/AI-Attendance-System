import cv2
import os
import numpy as np
from PIL import Image


dataset_path = "dataset"

model_path = "models"


if not os.path.exists(model_path):
    os.makedirs(model_path)



face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


faces = []
ids = []

labels = {}

current_id = 0



for student_id in os.listdir(dataset_path):


    folder_path = os.path.join(
        dataset_path,
        student_id
    )


    if not os.path.isdir(folder_path):
        continue


    current_id += 1


    labels[current_id] = student_id



    for image_name in os.listdir(folder_path):


        image_path = os.path.join(
            folder_path,
            image_name
        )


        try:

            img = Image.open(
                image_path
            ).convert("L")


            img_numpy = np.array(img)


            detected_faces = face_detector.detectMultiScale(
                img_numpy
            )


            for (x,y,w,h) in detected_faces:


                faces.append(
                    img_numpy[y:y+h,x:x+w]
                )


                ids.append(
                    current_id
                )


        except Exception as e:

            print(
                "Error:",
                image_path,
                e
            )



print(
    "Total Faces:",
    len(faces)
)



recognizer = cv2.face.LBPHFaceRecognizer_create()


recognizer.train(
    faces,
    np.array(ids)
)



recognizer.save(
    "models/trainer.yml"
)



with open(
    "models/labels.txt",
    "w"
) as file:


    for key,value in labels.items():

        file.write(
            f"{key},{value}\n"
        )



print("✅ Training Completed")
print(labels)