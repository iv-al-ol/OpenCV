import cv2
import numpy as np

img = cv2.imread("shema3.jpg")  # считывание рисунка
new_img = np.zeros((500, 500), np.uint8)

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 150)

cont, hier = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # получение контуров

#print(cont)

cv2.drawContours(new_img, cont, -1, (200, 200, 200), 1)  # рисунок по контурам

cv2.imshow("Result", new_img)  # вывод рисунка
cv2.waitKey(0)  # ожидание выведенного рисунка
