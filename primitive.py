import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype=np.uint8)  # создание матрицы изображений

#BGR - перевернутый формат RGB
color = (100, 100, 100)

#photo[:] = color  # заливка всей маски в цвет
#photo[100:150, 200:280] = color  # заливка прямоугольником

cv2.rectangle(photo, (10, 10), (400, 400), color, 2)  # выделение прямоугольником
cv2.line(photo, (23, 43), (143, 365), (color), 3)  # линия
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 50, color, 5)  # круг

cv2.putText(photo, "Alexey", (10, 400), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)  # вывод текста

cv2.imshow('Photo', photo)  # вывод матрицы изображения
cv2.waitKey(0)  # ожидание вывода
