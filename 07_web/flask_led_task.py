from flask import Flask
import RPi.GPIO as GPIO

Rled = 4; Bled = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(Rled, GPIO.OUT)
GPIO.setup(Bled, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def mainPage():
    return '''
        <h1> Main Page </h1>
        <h2> RED LED  <a href="led/red/on">on</a> <a href="/led/red/off">off</a></h2>
        <h2> BLUE LED  <a href="led/blue/on">on</a> <a href="/led/blue/off">off</a></h2><br>
    '''

@app.route("/led/<color>/<status>")
def led(color, status):
    if color == "red":
        if status == "on":
            GPIO.output(Rled, GPIO.HIGH)
            return '''
                <h1>RED LED ON</h1>
                <h2><a href="/">Go Main Page</a></h2>
            '''
        elif status == "off":
            GPIO.output(Rled, GPIO.LOW)
            return '''
                <h1>RED LED OFF</h1>
                <h2><a href="/">Go Main Page</a></h2>
            '''
    
    elif color == "blue":
        if status == "on":
            GPIO.output(Bled, GPIO.HIGH)
            return '''
                <h1>BLUE LED ON</h1>
                <h2><a href="/">Go Main Page</a></h2>
            '''
        elif status == "off":
            GPIO.output(Bled, GPIO.LOW)
            return '''
                <h1>BLUE LED OFF</h1>
                <h2><a href="/">Go Main Page</a></h2>
            '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
