import cv2

# 0 카메라로 촬영 파일이름 : 해당 동영상 재생하기
cap = cv2.VideoCapture('output.avi') # 카메라 장치 열기

if not cap.isOpened():
    print('Camera open failed')
    exit()

# 카메라 사진 찍기
# ret, frame = cap.read()
# cv2.imshow('frame',frame)
# cv2.imwrite('output.jpg',frame)
# cv2.waitKey(0)

#fourcc(four character code)
#divx(avi), mp4v(mp4), x264(h264)
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

while True:
    ret, frame = cap.read() # 현재 프레임 영상 출력

    if not ret:
        break

    cv2.imshow('frame',frame)
    # out.write(frame)
    if cv2.waitKey(10) == 27: # 10ms 기다린 후 다음 프레임 처리
        break

# 사용자 자원 해제

cap.release()
# out.release()
cv2.destroyAllWindows()