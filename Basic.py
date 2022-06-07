#import cv2
#import numpy as np
#import face_recognition

#imgWills = face_recognition.load_image_file('ImagesBasic/wills.jpg')
#imgWills = cv2.cvtColor(imgWills,cv2.COLOR_BGR2RGB)
#imgTest = face_recognition.load_image_file('ImagesBasic/wills1.jpg')
#imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)


#faceLoc = face_recognition.face_locations(imgWills)[0]
#encodeWills = face_recognition.face_encodings(imgWills)[0]
#cv2.rectangle(imgWills,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

#faceLocTest = face_recognition.face_locations(imgTest)[0]
#encodeTest = face_recognition.face_encodings(imgTest)[0]
#cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

#result = face_recognition.compare_faces([encodeWills],encodeTest)
#faceDis = face_recognition.face_distance([encodeWills],encodeTest)
#print(result,faceDis)
#cv2.putText(imgTest,f'{result} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


#cv2.imshow('Will Smith',imgWills)
#cv2.imshow('Will Test',imgTest)
#cv2.waitKey(0)
