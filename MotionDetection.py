import cv2

def MotionDetect():
    video_capture = cv2.VideoCapture(0)
    print("Press q to quit")
    
    last_frame = None
    frame = None
    while True:
        if (frame is not None):
            last_frame = gray
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if (last_frame is None):
            last_frame = gray

        #Calculating the difference on intensity between current and last image
        difference = cv2.absdiff(last_frame, gray)

        #pixel with a difference of more than x will turn black,
        #other will turn white
        thresh_diff = cv2.threshold(difference, 3, 255, cv2.THRESH_BINARY)[1]

        #Reduce noise
        thresh_diff = cv2.erode(thresh_diff, (5,5), iterations=2)
        thresh_diff = cv2.dilate(thresh_diff, (5,5), iterations=2)
                
        cnts, _ = cv2.findContours(thresh_diff.copy(), cv2.RETR_EXTERNAL, 
                                    cv2.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            #Number of pixel that must be white to create a box around it
            if cv2.contourArea(contour) > 1000: 
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 3)

        cv2.imshow('x', thresh_diff)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    MotionDetect()
