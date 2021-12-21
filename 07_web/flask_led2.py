from flask import Flask, render_template
import RPi.GPIO as GPIO


LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html", title="Hello, Flask!!")

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, 1)
        return "LED ON"
    
    elif op == "off":
        GPIO.output(LED_PIN, 0)
        return "LED OFF"
    
    else:
        return "Error"
    


# @app.route("/LED/ON")
# def LED_on():
#     return '''
#         <p>LED_ON</p>
#         <a href="/">Go Home</a>
#     '''

# @app.route("/LED/OFF")
# def LED_off():
#     return '''
#         <p>LED_OFF</p>
#         <a href="/">Go Home</a>
#     '''

# 터미널에서 직접 실행시켰다면
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
    
