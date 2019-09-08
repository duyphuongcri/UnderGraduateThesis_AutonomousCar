import RPi.GPIO as GPIO
import time
import serial                   
servoPIN = 19
frequency = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)    
pwm=GPIO.PWM(servoPIN,frequency) # 50hz

#3ser=serial.Serial('/dev/ttyUSB0',9600)


steer=130
duty_cycle_s= 2 + 1/18*steer
pwm.start(duty_cycle_s)    
class control:
    def control_steer(steer):
        duty_cycle= 2 + 1/18*steer
        pwm.ChangeDutyCycle(duty_cycle)

    def control_speed(signal):
        ser.write(signal)
