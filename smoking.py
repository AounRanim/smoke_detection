import cv2
import cvzone 
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector
Hand_Detector= HandDetector()
MeshDetector=FaceMeshDetector()

video=cv2.VideoCapture('C:\\Users\\HP\\Desktop\\ranim\\smoking.mp4')
point11x=point11y=0 # hand point
while True:
  ret,image=video.read()
  img,faces=MeshDetector.findFaceMesh(image,draw=True)
  results=Hand_Detector.findHands(image,draw=True)
  if len(results[0])>0:
    landmarks=results[0][0]['lmList']
    point11x,point11y=landmarks[11][0],landmarks[11][1]
    print(point11x,point11y)
  point14=faces[0][14] # lip point
  distance=MeshDetector.findDistance((point11x,point11y),(point14[0],point14[1]))[0]
  print(distance) 
  if distance < 40 :
    cvzone.putTextRect(image ,'Smoking' , (30,50))
  else :
    cvzone.putTextRect(image , 'No smoking' , (30,50))
    cv2.imshow('video' , image)
  if cv2.waitKey(10) == ord('q'):
        break 
  
cv2.destroyAllWindows()













