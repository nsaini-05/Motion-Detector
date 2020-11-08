import cv2
first_frame = None
video = cv2.VideoCapture(0)


while True:
    check , frame = video.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray , (21,21) , 0)

    if first_frame is None:
        first_frame = gray
        continue


    delta_frame = cv2.absdiff(first_frame , gray)
    thresh_delta = cv2.threshold(delta_frame , 30 , 255 ,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta , None , iterations =2)
    contours, hierarchy = cv2.findContours(thresh_delta, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)












    cv2.imshow("Frame", frame)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("Threshdelta" , thresh_delta)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break




video.release()
cv2.destroyAllWindows