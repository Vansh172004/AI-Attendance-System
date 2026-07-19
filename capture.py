import cv2
import os


# =============================
# Student ID
# =============================

student_id = input("Enter Student ID: ").strip()


# =============================
# Create Dataset Folder
# =============================

dataset_path = os.path.join(
    "dataset",
    student_id
)

os.makedirs(
    dataset_path,
    exist_ok=True
)


# =============================
# Open Camera
# =============================

camera = cv2.VideoCapture(0)


camera.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    640
)

camera.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    480
)


if not camera.isOpened():

    print("❌ Camera not found!")
    exit()



# =============================
# Face Detector
# =============================

face_detector = cv2.CascadeClassifier(

    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"

)


if face_detector.empty():

    print("❌ Haar Cascade Not Loaded!")
    exit()



# =============================
# Capture Count
# =============================

count = 0


print("\n📷 Camera Started...")
print("Look at Camera")
print("Press Q to Exit\n")



# =============================
# Camera Loop
# =============================

while True:


    ret, frame = camera.read()


    if not ret:

        print("❌ Camera Frame Error")
        break



    gray = cv2.cvtColor(

        frame,

        cv2.COLOR_BGR2GRAY

    )


    # Improve Light

    gray = cv2.equalizeHist(gray)



    faces = face_detector.detectMultiScale(

        gray,

        scaleFactor=1.1,

        minNeighbors=5,

        minSize=(100,100)

    )



    for (x,y,w,h) in faces:


        # Crop Face

        face = gray[
            y:y+h,
            x:x+w
        ]



        # Resize For Training

        face = cv2.resize(

            face,

            (200,200)

        )



        # Save Image

        if count < 100:


            count += 1


            file_path = os.path.join(

                dataset_path,

                f"{count}.jpg"

            )


            cv2.imwrite(

                file_path,

                face

            )



        # Face Box

        cv2.rectangle(

            frame,

            (x,y),

            (x+w,y+h),

            (0,255,0),

            2

        )



        # Text Display

        cv2.putText(

            frame,

            f"{student_id} Captured : {count}/100",

            (10,30),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0,255,0),

            2

        )




    # Show Camera

    cv2.imshow(

        "Face Capture",

        frame

    )



    key = cv2.waitKey(1) & 0xff



    if key == ord('q'):

        break



    if count >= 100:

        break



# =============================
# Close Camera
# =============================

camera.release()

cv2.destroyAllWindows()



print(
    f"\n✅ Successfully Captured {count} Images for {student_id}"
)