import cv2
import pytesseract.pytesseract


def show_image(window_name, frame, delay):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, frame)
    key = cv2.waitKey(delay)


def load_image(image_path):
    frame = cv2.imread(image_path)

    return frame


def filter_image(frame):
    crop = 100

    for i in range(0, 300, crop):
        for j in range(0, 300, crop):
            roi = frame[i: i + crop, j: j + crop]

            show_image('crop ', roi[5:90, 5:90], 1)

            ocr(roi[5:90, 5:90])


def image_parser(frame):
    filter_image(frame)

    # ocr(ret)


def ocr(frame):
    target = pytesseract.image_to_string(frame, lang='eng',
                                         config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(target)


if __name__ == '__main__':
    path = './test1.png'

    image = load_image(path)

    image_parser(image)
