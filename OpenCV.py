import cv2

carga = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')

imagem = cv2.imread('teste/imagem.jpg')

imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carga.detectMultiScale(imagemcinza)

print(faces)

for (x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow('Faces', imagem)
cv2.waitKey()
