import RPi.GPIO as GPIO #run code as admin
import time
 
GPIO.setmode(GPIO.BOARD) #GPIO.BCM : Pin Name. .BOARD : Pin Number by Order 
#GPIO.setmode(GPIO.BCM)

pwm = 10 #change pinnumber when use RPI. This is according to Arduino sample
in1 = 11
in2 = 12
vcc = 13 

#pin mode setup
GPIO.setup(pwm, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(vcc, GPIO.OUT) 

#digital write vcc high
GPIO.output(vcc, GPIO.HIGH)


def go(speed, time, forward):
    pwmPin = GPIO.PWM(pwm,1000)
    if(forward):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
    else:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)

    
    #code

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    

def turn(degree):
    pass
    #code