from lcd import drivers
import Adafruit_DHT
import datetime
import time
import threading

display = drivers.Lcd()
DHT_sensor = Adafruit_DHT.DHT11
DHT_PIN = 17

def DHT_Update():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_sensor, DHT_PIN)
    display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%", 2)

def timeUpdate():
    currentDateTime = datetime.datetime.now()
    display.lcd_display_string(currentDateTime.strftime("%x%X"), 1)

try:
    while True:
        currentDateTime = datetime.datetime.now()
        display.lcd_display_string(currentDateTime.strftime("%x%X"), 1)
        humidity, temperature = Adafruit_DHT.read_retry(DHT_sensor, DHT_PIN)

        if (humidity is not None and temperature is not None):
            display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%", 2)

finally:
    
    print("Cleaning up")
    display.lcd_clear()