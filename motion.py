import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
while True:
    ret, new1 = cap.read()
    new2 = cap.read()[1]
    d1=cv2.absdiff(new2, new1)
    d2=cv2.absdiff(new1, frame)

    d=cv2.bitwise_and(d1, d2)
    canny = cv2.Canny(d, 200, 100)
    contours = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]
    cv2.drawContours(frame, contours, -1, (255,0,0), 3)
    cv2.imshow('motion', canny)
    cv2.imshow('motion', frame)
    frame = new1
    new1=new2
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
