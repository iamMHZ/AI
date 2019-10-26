import cv2
import pytesseract.pytesseract
import numpy as np


def show_image(window_name, frame, delay):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, frame)
    key = cv2.waitKey(delay)


def load_image(image_path):
    frame = cv2.imread(image_path)

    return frame


def filter_image(frame):
    crop = 100

    numbers = []

    for i in range(0, 300, crop):
        for j in range(0, 300, crop):
            roi = frame[i: i + crop, j: j + crop]

            # pre processing
            _, roi = cv2.threshold(roi, 20, 255, cv2.THRESH_BINARY)
            kernel = np.ones((3, 3), np.int)
            roi = cv2.erode(roi, kernel)
            roi = cv2.GaussianBlur(roi, (3, 3), 0)

            # show_image('crop ', roi[5:90, 5:90], 0)

            number = ocr(roi[5:90, 5:90])

            numbers.append(number)

    return numbers


def image_parser(image_path):
    # load image
    frame = load_image(image_path)

    numbers = filter_image(frame)

    return numbers


def ocr(frame):
    target = pytesseract.image_to_string(frame, lang='eng',
                                         config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(target)

    return target


if __name__ == '__main__':
    path = './test3.png'

    image = load_image(path)

    image_parser(image)
