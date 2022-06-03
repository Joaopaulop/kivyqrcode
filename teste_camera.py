import cv2
from pyzbar.pyzbar import decode
from PIL import Image 
from qrapp2 import lerQR as dcd

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if webcam.isOpened():
   validacao, frame = webcam.read()
   while validacao:
      validacao, frame = webcam.read()
      cv2.imshow("Video da Webcam", frame)
      key = cv2.waitKey(2)
      if cv2.waitKey(33) == ord('a'):
         cv2.imwrite("Foto.png",frame)
         dcd.lerQR()
         break
      
      #cv2.imwrite("Foto.png",frame)
webcam.release()


cv2.destroyAllWindows()



