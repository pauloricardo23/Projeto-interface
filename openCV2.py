import cv2

carga = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
imagem= cv2.imread('Fotos/imagem3.jpg')
imagemcinza = 0
imagem = imagemcinza
imagemcinza= cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
face = carga.detectMultiScale(imagemcinza)
