import RPi.GPIO as GPIO
import cv2
import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# 점수
score = 0

# OLED 초기 세팅
RESET_PIN = digitalio.DigitalInOut(board.D4)
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=RESET_PIN)
oled.fill(0)
oled.show()
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# 시작 시 OLED에 문구 표시
print("Shot a vaccine on people.")
draw.text((0, 0), 'Shot a vaccine', font=font2, fill=255)
draw.text((5, 13),'on people', font=font2, fill=255)
draw.text((0, 27), "Save the world", font=font2, fill=255)
draw.text((0, 40), "from a virus!", font=font2, fill=255)
oled.image(image)
oled.show()

# Button Pin : 서보모터 왼쪽 오른쪽 조절 
Bl = 5; Br = 6
# Button Pin : shot 버튼
A1 = 25

# GPIO 세팅
GPIO.setmode(GPIO.BCM)
GPIO.setup(Bl, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Br, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(A1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.OUT)

# 서보모터 설정
_Servo = GPIO.PWM(19, 50)
_Duty = 9
_Servo.start(9)

# xml 파일 로드 & 카메라 열기
body_cascade = cv2.CascadeClassifier('./xml/body.xml')
camera = cv2.VideoCapture(0)

# 마지막으로 카메라를 읽은 시간 : 카메라를 3000ms마다 읽어오려고 사용
lastCamReadTime = 0

# 카메라가 열리지 않은 경우 종료
if not camera.isOpened():
    print('Camera open failed')
    exit()

# 이미지 90도 회전
def Rotate(src):
    dst = cv2.transpose(src) # 행렬 변경 
    dst = cv2.flip(dst, 1)   # 뒤집기
        
    return dst

try:
    while True:
        if time.time() - lastCamReadTime >= 0.3: # 3000ms마다 if 안 코드 실행
            ret, frame = camera.read()
            lastCamReadTime = time.time()

            if not ret:
                break

            frame = Rotate(frame) # 이미지 회전
            body = body_cascade.detectMultiScale(frame, 1.1, 5) # 사람 전체 모습 검출

            for(x, y, w, h) in body:

                if x < 245 and 245 < x + w and y < 305 and 305 < y + h: # 조준점이 검출된 객체 내부에 있다면
                    if GPIO.input(A1): # shot 버튼을 눌렀을 때
                        # score 증가
                        score += 1

                        # 증가한 Score 표시
                        oled.fill(0)
                        oled.show()
                        image = Image.new("1", (oled.width, oled.height))
                        draw = ImageDraw.Draw(image)
                        draw.text((0, 0), f'Score : {score}', font=font, fill=255)
                        oled.image(image)
                        oled.show()

                # 검출한 객체 위치 그리기
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            # 조준점 그리기
            cv2.rectangle(frame, (240, 300), (250, 310), (255,0,0), 2)

            # 촬영한 사진 + 조준점과 객체 위치가 그려진 이미지 표시
            cv2.imshow('frame', frame)

        if GPIO.input(Br): # 오른쪽 버튼을 눌렀을 때 서보모터 회전
            if _Duty >= 6: # 버튼을 누를때 조금씩 움직이다가 일정 각도 이상 움직이면 멈춤
                _Duty -= 0.3
                _Servo.ChangeDutyCycle(_Duty)
        
        elif GPIO.input(Bl): # 왼쪽 버튼을 눌렀을 때 서보모터 회전
            if _Duty <= 11: # 버튼을 누를때 조금씩 움직이다가 일정 각도 이상 움직이면 멈춤
                _Duty += 0.3
                _Servo.ChangeDutyCycle(_Duty)

        if cv2.waitKey(1) == ord("q"): # q 키를 눌렀을 때 종료
                break
        
finally: # 자원 해제
    camera.release()
    cv2.destroyAllWindows()
    _Servo.stop()
    GPIO.cleanup()
    
camera.release()
cv2.destroyAllWindows()
_Servo.stop()
GPIO.cleanup()

