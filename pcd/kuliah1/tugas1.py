import cv2 as cv
import numpy as np

img1 = cv.imread("gelap.jpg");
img2 = cv.imread("terang.jpg");
img3 = cv.imread("lowContrast.jpg");
img4 = cv.imread("highContrast.jpg");
img5 = cv.imread("custom.jpg");

def linear(image, alpha, beta):
    b = alpha * image[:, :, 0].astype(np.int16) + beta;
    g = alpha * image[:, :, 1].astype(np.int16) + beta;
    r = alpha * image[:, :, 2].astype(np.int16) + beta;
    return np.clip(np.stack([b, g, r], axis=2), 0, 255).astype(np.uint8)

def negative(image):
    return linear(image, -1, 255);

def bgrToGrayscale(image):
    b = image[:, :, 0].astype(np.float32);
    g = image[:, :, 1].astype(np.float32);
    r = image[:, :, 2].astype(np.float32);
    return (.299 * r + .587 * g + .114 * b).astype(np.uint8);

def threshold(image, thresholdValue):
    image = bgrToGrayscale(image);                                   
    return np.where(image > thresholdValue, 0, 255).astype(np.uint8);

def gamma(image, constant, gamma):
    b = constant * (image[:, :, 0].astype(np.float32) ** gamma);
    g = constant * (image[:, :, 1].astype(np.float32) ** gamma);
    r = constant * (image[:, :, 2].astype(np.float32) ** gamma);
    return np.clip(np.stack([b, g, r], axis=2), 0, 255).astype(np.uint8)

def getImage():
    match(input("""
1. Gelap
2. Terang
3. Kontras Rendah
4. Kontras Tinggi
5. Kombinasi
Pilih satu [1]:
""")):
        case '1':
            return img1;
        case '2':
            return img2;
        case '3':
            return img3;
        case '4':
            return img4;
        case '5':
            return img5;
        case _:
            return img1;

def manualInput():
    match(input("""
1. Negative
2. Linear
3. Gamma
4. Threshold
Pilih satu [1]:
""")):
        case '1':
            cv.imshow("result", negative(getImage()));
        case '2':
            cv.imshow("result", linear(getImage(), int(input("Alpha: ")), int(input("Beta: "))));
        case '3':
            cv.imshow("result", gamma(getImage(), int(input("c: ")), int(input("Gamme: "))))
        case '4':
            cv.imshow("result", threshold(getImage(), int(input("Threshold: "))))
        case _:
            cv.imshow("result", negative(getImage()));

def slider():
    match(input("""
1. Negative
2. Linear
3. Gamma
4. Threshold
Pilih satu [1]:
""")):
        case '1':
            cv.imshow("result", negative(getImage()));
            cv.waitKey(1);
        case '2':
            img = getImage()
            cv.namedWindow("result")
            cv.createTrackbar("Alpha x10", "result", 10, 50, lambda x: None)  # 1.0–5.0
            cv.createTrackbar("Beta", "result", 0, 255, lambda x: None)

            while True:
                cv.imshow("result", linear(img, cv.getTrackbarPos("Alpha x10", "result") / 10.0, cv.getTrackbarPos("Beta", "result")));
                if cv.waitKey(1) & 0xFF == 27:  # ESC
                    break;
        case '3':
            img = getImage()
            cv.namedWindow("result")
            cv.createTrackbar("Gamma x10", "result", 10, 50, lambda x: None)
            cv.createTrackbar("c", "result", 1, 10, lambda x: None)

            while True:
                cv.imshow("result", gamma(img, cv.getTrackbarPos("c", "result"), max(cv.getTrackbarPos("Gamma x10", "result") / 10.0, 0.1)));
                if cv.waitKey(1) & 0xFF == 27:  # ESC
                    break;
        case '4':
            img = getImage()
            cv.namedWindow("result")
            cv.createTrackbar("Threshold", "result", 127, 255, lambda x: None)

            while True:
                cv.imshow("result", threshold(img, cv.getTrackbarPos("Threshold", "result")));
                if cv.waitKey(1) & 0xFF == 27:  # ESC
                    break;
        case _:
            cv.imshow("result", negative(getImage()));
            cv.waitKey(1);

def main():
    match(input("1. Slider\n2. Manual Input [1]:\n")):
        case "1":
            slider();
        case "2":
            manualInput();
        case _:
            slider();
