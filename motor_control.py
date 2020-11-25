import RPi.GPIO as GPIO #run code as admin
 
GPIO.setmode(GPIO.BOARD) #GPIO.BCM : Pin Name. .BOARD : Pin Number by Order 
#GPIO.setmode(GPIO.BCM)

pwm = 10 #change pinnumber when use RPI. This is according to Arduino sample
in1 = 11
in2 = 12
vcc = 13 

GPIO.setup(pwm, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(vcc, GPIO.OUT) 
GPIO.output(vcc, GPIO.HIGH)



def go(speed):
    pass
    #code

def turn(degree):
    pass
    #code