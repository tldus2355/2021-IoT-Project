import cv2

face_cascade = cv2.CascadeClassifier('./xml/face.xml')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read() # 현재 프레임 영상 출력

    if not ret:
        break
    
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(50) == 27: # 10ms 기다린 후 다음 프레임 처리
        break

# 사용자 자원 해제
cap.release()
# out.release()
cv2.destroyAllWindows()