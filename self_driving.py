import cv2 as cv
import pickle
import numpy as np
#from picamera import PiCamera
#from motor_control import go, turn
from time import time

Wheel_base = 700 #앞바퀴 중심 ~ 뒷바퀴 중심
Wheel_width = 670 #뒷바퀴 간격

def lanesDetection(img):
    # img = cv.imread("./img/road.jpg")
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    region_of_interest_vertices = [
        (200, height), (width/2, height/2), (width-300, height)
    ]
    #gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    #ret, thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)
    img = cv.bilateralFilter(img, 15,75,75) #IS SLOW
    edge = cv.Canny(img, 300,400, apertureSize=3)
    cropped_image = region_of_interest(
        edge, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(cropped_image, rho=2, theta=np.pi/180,
                           threshold=50, lines=np.array([]), minLineLength=10, maxLineGap=30)
    image_with_lines = draw_lines(img, lines)
    # plt.imshow(image_with_lines)
    # plt.show()
    return image_with_lines


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = (255)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    if lines is None:
        return img
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def videoLanes(camera):
    cap = cv.VideoCapture(camera)
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = lanesDetection(frame)
        cv.imshow('Lanes Detection', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

def follow_line(speed,fps):
    #camera = PiCamera()
    #camera = "./test_image/test_vid.MOV"
    camera = 0
    videoLanes(camera)

if __name__ == '__main__':
    # TODO: Initialize camera from calibration file
    follow_line(0,0)