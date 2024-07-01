import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Aplicar la transformada de Hough para detectar circunferencias
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)

# Mostrar la imagen con las circunferencias detectadas
cv2.imshow('Transformada de Hough para Circunferencias', image)
cv2.waitKey(0)
cv2.destroyAllWindows()