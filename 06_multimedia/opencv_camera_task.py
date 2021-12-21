import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read() # 현재 프레임 영상 출력

    if not ret:
        break

    edge = cv2.Canny(frame, 30, 80)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('original', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27: # 10ms 기다린 후 다음 프레임 처리
        break

cap.release()
cv2.destroyAllWindows()
