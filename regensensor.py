import RPi.GPIO as GPIO
import time

print("hoi")

GPIO.setmode(GPIO.BCM)

REGENPIN = 23

GPIO.setup(REGENPIN, GPIO.IN)

is_regen = GPIO.input(REGENPIN)

while True:
    print(is_regen)
    time.sleep(2)