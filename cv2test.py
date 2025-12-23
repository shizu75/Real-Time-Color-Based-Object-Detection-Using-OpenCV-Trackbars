import cv2
import numpy as np

cao = cv2.VideoCapture(0)

def python(x):
    pass

cv2.namedWindow('Object_Detection')

cv2.createTrackbar('th', 'Object_Detection', 0 ,255, python)

cv2.createTrackbar('lb', 'Object_Detection', 0 ,255, python)
cv2.createTrackbar('lg', 'Object_Detection', 0 ,255, python)
cv2.createTrackbar('lr', 'Object_Detection', 0 ,255, python)

cv2.createTrackbar('ub', 'Object_Detection', 255 ,255, python)
cv2.createTrackbar('ug', 'Object_Detection', 255 ,255, python)
cv2.createTrackbar('ur', 'Object_Detection', 255 ,255, python)

while cao.isOpened():
    r, img = cao.read()
    if r == True:
        img = cv2.resize(img, (400, 300))
        img = cv2.flip(img, 1)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        thr = cv2.getTrackbarPos('th', 'Object_Detection')
        
        Lb = cv2.getTrackbarPos('lb', 'Object_Detection')
        Lg = cv2.getTrackbarPos('lg', 'Object_Detection')
        Lr = cv2.getTrackbarPos('lr', 'Object_Detection')

        Ub = cv2.getTrackbarPos('ub', 'Object_Detection')
        Ug = cv2.getTrackbarPos('ug', 'Object_Detection')
        Ur = cv2.getTrackbarPos('ur', 'Object_Detection')

        lo = np.array([Lb, Lg, Lr])
        up = np.array([Ub, Ug, Ur])

        masks = cv2.inRange(hsv_img, lo, up)
        res = cv2.bitwise_and(img, img, mask = masks)
        fr = cv2.bitwise_not(res)
        r, thi = cv2.threshold(masks, thr, 255, cv2.THRESH_BINARY)

        c, h = cv2.findContours(thi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, c, -1, (255,0,0), 2)
        cv2.imshow('thr', thi)

        img = np.array(img)
        hsv_img = np.array(hsv_img)
        masks = np.stack((masks,)*3, axis = -1)
        res = np.array(res)

        h = np.hstack((img, masks))
        g = np.hstack((res, hsv_img))
        ri = np.vstack((h,g))
        
        cv2.imshow('IMAGE', ri)
        

        if cv2.waitKey(25) & 0xFF == ord('p'):
            break

    else:
        break

cao.release()
cv2.destroyAllWindows()
