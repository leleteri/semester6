import os
import numpy as np
import cv2

image = cv2.imread("furia.jpg")
if image is None:
    raise FileNotFoundError("furia.jpg not found")

row, col, ch = image.shape

# Nomor 1
kanvas1 = np.zeros((row, col, 3), np.uint8)
for i in range(row):
    for j in range(col):
        kanvas1[i, j] = image[i, j]

# Nomor 2
kanvas2 = kanvas1.copy()
for i in range(row):
    for j in range(col):
        for k in range (3):
            if (kanvas2[i, j, k] < 150):
                kanvas2[i, j, k] = 255

# Nomor 3
kanvas3 = np.zeros((col, row, 3), np.uint8)
for i in range(row):
    for j in range(col):
        kanvas3[j, i] = kanvas1[i, j]

match input(
    "0. Print Matrix\n"
    "1. Print Gambar Soal1\n"
    "2. Print Gambar Soal2\n"
    "3. Print Gambar Soal3\n"
    "Pilih Salah Satu [default 1]: "
):
    case '0':
        for i in range(10):
            for j in range(10):
                print(str(kanvas1[i, j]) + " ", end="")
            print("\n")
        exit()
    case '1':
        cv2.imshow("Gambar pada Kanvas", kanvas1)
    case '2':
        cv2.imshow("Gambar pada Kanvas", kanvas2)
    case '3':
        cv2.imshow("Gambar pada Kanvas", kanvas3)
    case _:
        cv2.imshow("Gambar Pada Kanvas", kanvas1)

cv2.waitKey(0)
cv2.destroyAllWindows
