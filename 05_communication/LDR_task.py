import RPi.GPIO as GPIO
import spidev
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

spi = spidev.SpiDev()


spi.open(0, 0)


spi.max_speed_hz = 100000


def analog_read(channel):
    
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    print(ret)
    adc_out = ((ret[1] & 3) << 8)  + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0)
        print("Reading = %d, Voltage = %f" % (reading,reading*3.3/1024))

        if (reading < 550) :
            GPIO.output(LED_PIN, GPIO.HIGH)
        else :
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
finally : 
    spi.close()
