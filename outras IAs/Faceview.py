import cv2

print("Code completed")

trained_Data = cv2.CascadeClassifier('facerecognizer.xml')

image = cv2.imread("Imagem.jpg")


newimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_coordinates = trained_Data.detectMultiScale(newimg)

print(face_coordinates)