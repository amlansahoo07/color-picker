import cv2
import numpy as np

# Function definition borrowed from cvzone library by Computer Vision Zone
# Website: https://www.computervision.zone/
def stackImages(scale,imgArray):
    """
    Stacks images either horizontally or vertically for display.

    Parameters:
        scale (float): Scaling factor for resizing images.
        imgArray (list): List containing images to be stacked. Images can be arranged either horizontally or vertically.

    Returns:
        numpy.ndarray: Stacked image.
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# Dummy callback function
def nothing(x):
    """
    Dummy function used as a callback for trackbars.

    Parameters:
        x (int): Trackbar position value (not used).
    """
    pass

def main():

    cv2.namedWindow('Trackbars')
    cv2.resizeWindow("Trackbars",640,240)

    cv2.createTrackbar('Hue Min', 'Trackbars', 29, 179, nothing)
    cv2.createTrackbar('Hue Max', 'Trackbars', 43, 179, nothing)
    cv2.createTrackbar('Saturation Min', 'Trackbars', 10, 255, nothing)
    cv2.createTrackbar('Saturation Max', 'Trackbars', 255, 255, nothing)
    cv2.createTrackbar('Value Min', 'Trackbars', 100, 255, nothing)
    cv2.createTrackbar('Value Max', 'Trackbars', 255, 255, nothing)


    while True:

        # Photo by @keskinlerinmehmet on Unsplash
        img = cv2.imread('apple.jpg')
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Get current positions of all trackbars
        h_min = cv2.getTrackbarPos('Hue Min', 'Trackbars')
        h_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
        s_min = cv2.getTrackbarPos('Saturation Min', 'Trackbars')
        s_max = cv2.getTrackbarPos('Saturation Max', 'Trackbars')
        v_min = cv2.getTrackbarPos('Value Min', 'Trackbars')
        v_max = cv2.getTrackbarPos('Value Max', 'Trackbars')

        # Logger for printing current HSV values
        # print(h_min,h_max,s_min,s_max,v_min,v_max)
        
        # Set the HSV range
        hsv_min = np.array([h_min, s_min, v_min])
        hsv_max = np.array([h_max, s_max, v_max])
        
        # Mask the image using the HSV range
        imgMask = cv2.inRange(imgHSV, hsv_min, hsv_max)
        # Apply the mask to the original image
        imgResult = cv2.bitwise_and(img, img, mask=imgMask)

        # cv2.imshow("Image", img)
        # cv2.imshow("ImageHSV", imgHSV)
        # cv2.imshow("ImageMask", mask)
        # cv2.imshow("ImageResult", result)

        imgStack = stackImages(0.6,([img,imgHSV], [imgMask, imgResult]))
        cv2.imshow("Stacked Images", imgStack)

        key = cv2.waitKey(1)
        if key == ord('q'):  # Press 'q' key to exit
                break

        # Check if the window is still open
        if cv2.getWindowProperty("Stacked Images", cv2.WND_PROP_VISIBLE) < 1:
            break
        cv2.waitKey(1)


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()