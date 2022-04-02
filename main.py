import cv2

def ImageScale(img, percent):
    height = img.shape[1]
    width = img.shape[0]
    new_scale = []
    new_height = (percent * height) // 100
    new_width = (percent * width) // 100
    new_scale.append(new_height)
    new_scale.append(new_width)
    return new_scale


img = cv2.imread("shema3.jpg")
img = cv2.GaussianBlur(img, (3, 5), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_height = img.shape[1]
img_width = img.shape[0]

new_img = cv2.resize(img, ImageScale(img, 45))

new_img_height = new_img.shape[1]
new_img_width = new_img.shape[0]

cv2.imshow("Result", new_img[0:(new_img_height - new_img_height//2), 0:(new_img_width - new_img_width//4)])

cv2.waitKey(0)
