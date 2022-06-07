import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDwsMe2DAn14vr9d9ELX0ArUZBi73nCEio",
    "authDomain": "facerecognitionproject-264cc.firebaseapp.com",
    "databaseURL": "https://facerecognitionproject-264cc-default-rtdb.firebaseio.com",
    "projectId": "facerecognitionproject-264cc",
    "storageBucket": "facerecognitionproject-264cc.appspot.com",
    "messagingSenderId": "549937822436",
    "appId": "1:549937822436:web:ae6ab7d2f0e501bd674af1",
    "measurementId": "G-SCJ3HM2JCG"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


path = 'ImagesAttendance'
url='http://192.168.231.162/cam-hi.jpg'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList




def markAttendance(name):
    now = datetime.now()
    dtString = now.strftime("%d/%m/%Y")
    d1 = now.strftime("%H:%M:%S")
    db.child("Attendance").child(name).child("name").set(name)
    db.child("Attendance").child(name).child("date").set(dtString)
    db.child("Attendance").child(name).child("time").set(d1)






encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Third step (Camera)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('ESP32', img)
    cv2.waitKey(1)
