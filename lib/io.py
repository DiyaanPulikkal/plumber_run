import RPi.GPIO as GPIO
from mpu6050 import mpu6050

GPIO.setmode(GPIO.BCM)

GREEN_LED = 21
RED_LED = 20
PULLDOWN_BUTTON = 16
mario = mpu6050(0x69)
luigi = mpu6050(0x68)
GPIO.setwarnings(False)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(PULLDOWN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 0 means red, 1 means green
def turn_on_led(color):
    if color == 1:
        GPIO.output(GREEN_LED, GPIO.HIGH)
        return
    GPIO.output(RED_LED, GPIO.HIGH)

def turn_off_led(color):
    if color == 1:
        GPIO.output(GREEN_LED, GPIO.LOW)
        return
    GPIO.output(RED_LED, GPIO.LOW)

def is_button_pressed():
    return GPIO.input(PULLDOWN_BUTTON) == GPIO.HIGH

# 0 means mario, 1 means luigi
def is_jumping(player):
    if player == 1:
        return luigi.get_accel_data()['y'] < 0
    return mario.get_accel_data()['y'] < 0

def is_walking_forward(player):
    if player == 1:
        return luigi.get_accel_data()['x'] < 0
    return mario.get_accel_data()['x'] < 0

def cleanup():
    GPIO.cleanup()