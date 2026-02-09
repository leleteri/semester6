import numpy as np
import cv2

# funsi ubah color channel manual
def bgrToHsv(img):
    row, col, _ = img.shape; # untuk mendapatkan jumlah pixel gambar
    hsvImg = bgrImg.copy();
    for i in range(row):
        for j in range(col):
            b, g, r = bgrImg[i, j]/255; # untuk mendapatkan nilai dari setiap channel di pixel saat ini
            cMax = np.maximum(np.maximum(r, g), b); # nilai maksimum antara channel
            cMin = np.minimum(np.minimum(r, g), b); # minimumnya
            delta = cMax - cMin

            # https://math.stackexchange.com/questions/556341/rgb-to-hsv-color-conversion-algorithm
            if cMax == r:
                h = (60 * ((g - b) / delta) + 360) % 360
            elif cMax == g:
                h = (60 * ((b - r) / delta) + 120)
            else:
                h = (60 * ((r - g) / delta) + 240)
            h = (h / 2).astype(np.uint8) # untuk range 0-179

            if cMax == 0:
                s = 0;
            else:
                s = delta / cMax;
            # untuk range 0-255
            s = (s * 255).astype(np.uint8);
            v = (cMax * 255).astype(np.uint8);

            img[i, j] = h, s, v;
    return img;

def threshold(img, th):
    row, col = img.shape;
    for i in range(row):
        for j in range(col):
            if img[i, j] < th:
                img[i, j] = 0;
            else:
                img[i, j] = 255;
    return img

img = cv2.imread("Lenna.png");
assert img is not None

hsv_img = bgrToHsv(img)
h, s, v = cv2.split(hsv_img);

rata2_h = float(np.mean(h));
rata2_s = float(np.mean(s));
rata2_v = float(np.mean(v));
h
h_2 = threshold(h, rata2_h);
s_2 = threshold(s, rata2_s);
v_2 = threshold(v, rata2_v);

cv2.imshow("HUE", h_2);
cv2.imshow("SATURATION", s_2);
cv2.imshow("VALUE", v_2);

cv2.waitKey(0);
