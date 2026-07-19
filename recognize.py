def recognize_face(frame):

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.equalizeHist(gray)


    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80,80)
    )


    print("Detected Faces:", len(faces))


    for (x,y,w,h) in faces:


        face = gray[y:y+h, x:x+w]


        face = cv2.resize(
            face,
            (200,200)
        )


        label, confidence = recognizer.predict(face)


        print(
            "LABEL:",
            label,
            "CONF:",
            confidence
        )


        student_id = labels.get(label)



        if student_id and confidence < 80:

            cv2.rectangle(
                frame,
                (x,y),
                (x+w,y+h),
                (0,255,0),
                2
            )


            cv2.putText(
                frame,
                student_id,
                (x,y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )


        else:

            cv2.putText(
                frame,
                "Unknown",
                (x,y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2
            )


    return frame