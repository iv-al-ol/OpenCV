import cv2
import numpy as np

def ImageScale(img, percent):
    """Функция масштабирования изображения"""
    height = img.shape[1]
    width = img.shape[0]
    new_scale = []
    new_height = (percent * height) // 100
    new_width = (percent * width) // 100
    new_scale.append(new_height)
    new_scale.append(new_width)
    return new_scale

def rotate(img, angle):
    """Функция поворота изображения"""
    height, width = img.shape[:2]
    point = (width//2, height//2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)  # функция масштабирования
    return cv2.warpAffine(img, mat, (width, height))

def transform(img, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, mat, (img.shape[1], img.shape[0]))

img = cv2.imread("shema3.jpg")  # считывание рисунка
img = cv2.GaussianBlur(img, (3, 5), 0)  # размытие рисунка
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # перевод рисунка в серый цвет
img = cv2.Canny(img, 50, 50)  # пороги, обводка, черный и белый цвет

kernel = np.ones((3, 3), np.uint8)  # создание матрицы с 1 с 3 строки, 3 столбцов
img = cv2.dilate(img, kernel, iterations=1)  # обводка
img = cv2.erode(img, kernel, iterations=1)  # уменьшение обводок

#img = cv2.flip(img, -1)  # отзеркаливание

#img = rotate(img, 20)  # вращение рисунка
#img = transform(img, 30, 30)  # смещение рисунка

img_height = img.shape[1]  # высота рисунка
img_width = img.shape[0]  # ширина рисунка

new_img = cv2.resize(img, ImageScale(img, 60))  # изменение размеров рисунка

new_img_height = new_img.shape[1]  # высота нового рисунка
new_img_width = new_img.shape[0]  # ширина нового рисунка

cv2.imshow("Result", new_img[50:(new_img_height//3 + new_img_height//10), 
                             100:(new_img_width//2 + new_img_width//4)])  # вывод рисунка
cv2.waitKey(0)  # ожидание выведенного рисунка
