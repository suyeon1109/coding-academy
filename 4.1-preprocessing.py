import cv2
import numpy as np


img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코1.jpg")

# #region of interest = roi (관심영역)
# x = 20; y = 50; w =50; h=50
# roi = img[y:y+h, x:x+w]

# print(roi.shape)
# #(50, 0, 3) 50 = 50가지의 디멘션 3d 안에서도 2d의 개수가 50개

# cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
# cv2.imshow("img", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#thresholding
"""
흑백사진의 정의 : binary image (0,255) 
일케 표현하는 ㅣㅇ유: 이미지에서 원하는 피사체의 모양을 좀 더 정확히 판단하기 위함.
종이에서 글씨를 분리, 배경에서 전경을 분리하는 작업 등

thresholding: 여러 점수를 커트라인 기준으로 합격 불합격으로 나누는 것처럼
여러 값을 경계점을 기준으로 두 가지로 분류로 나눈 것이다. 이렇게 나눠진 두가지
색 즉 흑,백이 바이너리 이미지를 만드는 가장 대표적인 방법이다.
"""

import matplotlib.pylab as plt
img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코6.jpg", cv2.IMREAD_GRAYSCALE)

print(img)

#numpy로 바이너리 이미지 만들어보기
thresh_np = np.zeros_like(img)
#print(thresh_np)
thresh_np[img>127] = 255   #0=black, 255=white

#openCV로 바이너리 이미지 만들어보기
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

imgs = {"Original": img, "Numpy": thresh_np, "OpenCV": thresh_cv}

# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(1,3,i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([]) #없어도 됨
# plt.show()




# img = cv2.imread("/Users/mac/Documents/GitHub/computer-vision/지코/지코1.jpg", cv2.IMREAD_GRAYSCALE)

# _, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# _, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# _, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# _, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# _, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# imgs = {"Original": img, "binary": t_bin, "bininv": t_bininv, "truc": t_truc, "t_2zr" : t_2zr, "2zrinv": t_2zrinv}

# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(2,3,i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([]) #없어도 됨
# plt.show()




#자동으로 이미지에 맞게 threshold 적용해주는 알고리즘
"""
Otsu -> Nobuyuki Otsu 가 만든 오츠 알고리즘
-> 유동적으로 사진에 맞는 threshold를 결정하기 위해 사용됨
"""
# _, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# _, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# _, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# _, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# _, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

_, t_130 = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
t, t_otsu = cv2.threshold(img,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print('otsu threshold:', t)

imgs = {"Original": img, "t_130": t_130, "otsu": t_otsu}

for i, (key,value) in enumerate(imgs.items()):
    plt.subplot(1,3,i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([]) #없어도 됨
plt.show()