import cv2
import time
import numpy as np
from mss import mss
import win32api
import win32con
import mouse
import math
#SIMPLE RECOIL CONTROL FOR PUBG Mobile BASED ON FEATURE TRACKING ALGORITHMS
#xNWRx
orb = cv2.ORB_create()

def orbDetectionAndCompute(img, img2):
    kp1, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    return matches, kp1, kp2


while 'playing':    
    with mss() as sct:
        monitor = {'top': 150, 'left': 205, 'width': 966, 'height': 466}#Here is defined the part of monitor you want to grab
        old_img = np.array(sct.grab(monitor))
        old_img = cv2.cvtColor(old_img, cv2.COLOR_BGR2GRAY)
                
        while mouse.is_pressed(button='middle'):
            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            matches, kp1, kp2 = orbDetectionAndCompute(old_img, img)
            xm = 0
            ym = 0

            for match in matches[:20]:
                x1,y1 = kp1[match.queryIdx].pt
                x2,y2 = kp2[match.trainIdx].pt
                xm += x2-x1
                ym += y2-y1
                    
            xm = xm/20
            ym = ym/20
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

            xm *= 0.4
            ym *= 0.4
            
            #if -2 > ym:
                #ym *= 0.5
                #ym = math.floor(ym)
            #elif ym > 2:
                #ym *= 0.5
                #ym = math.floor(ym)
            
            
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(math.floor(xm)), int(math.floor(ym)), 0, 0)
            time.sleep(0.008)#The game does not compute input if it's too fast, be sure to change the sleep time according to the time your machine is taking for computing ORB
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            