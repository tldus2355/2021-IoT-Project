from flask import Flask, render_template
import RPi.GPIO as GPIO

led = [4, 5]
ledColor = ["Red", "Blue"]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led[0], GPIO.OUT)
GPIO.setup(led[1], GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('button_led_control.html')

@app.route("/led/<color>/<op>")
def led(color, op):
    if color == '0':
        if op == "on":
            GPIO.output(4, 1)
            return "RED LED on"
        
        elif op == "off":
            GPIO.output(4, 0)
            return "RED LED off"

    elif color == '1':
        if op == "on":
            GPIO.output(5, 1)
            return "Blue LED on"
            
        elif op == "off":
            GPIO.output(5, 0)
            return "Blue LED off"

    return "Error"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
