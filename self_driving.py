import cv2
import pickle
import numpy as np
from picamera import PiCamera
from motor_control import Go, Turn
from time import time

Wheel_base = 700 #앞바퀴 중심 ~ 뒷바퀴 중심
Wheel_width = 670 #뒷바퀴 간격

def get_line(camera):
    def lanesDetection(img):
        height = img.shape[0]
        width = img.shape[1]

        region_of_interest_vertices = [
            (200, height), (width/2, height/1.37), (width-300, height)
        ]
        gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        edge = cv.Canny(gray_img, 50, 100, apertureSize=3)
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
    
    cap = cv.VideoCapture(camera)
    ret, frame = cap.read()
    frame = lanesDetection(frame)
    cv.imshow('Lanes Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

def follow_line(speed,fps):
    camera = PiCamera()
    


