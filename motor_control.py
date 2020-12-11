import RPi.GPIO as GPIO #run code as admin
import time
 
GPIO.setmode(GPIO.BOARD) #GPIO.BCM : Pin Name. .BOARD : Pin Number by Order 
#GPIO.setmode(GPIO.BCM)

enA = 4
stepPin = 5
dirPinLR = 6
pwm = 10 #change pinnumber when use RPI. This is according to Arduino sample
in1 = 11
in2 = 12
vcc = 13 

#pin mode setup
GPIO.setup([pwm,in1,in2,vcc,enA,stepPin,dirPinLR], GPIO.OUT)

#digital write vcc high
GPIO.output(vcc, GPIO.HIGH)

class MotorControl:
    def __init__(self):
        self.curVel = 0 #현재 속도
        self.curFor = True #현재 방향 (True가 전진)
        self.pwmPin = GPIO.PWM(pwm,1000)
        self.pwmPin.start(0)

    def go(self, speed, accelt, forward):
        
        if(forward):
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            if(not self.curFor):
                self.curVel = 0
                self.curFor = True
                pwm.ChangeDutyCycle(0)
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            if(self.curFor):
                self.curVel = 0
                self.curFor = False
                pwm.ChangeDutyCycle(0)
        
        initVel = self.curVel
        deltaVel = speed - initVel
        for i in range(10):
            self.curVel += deltaVel/10 
            self.pwmPin.ChangeDutyCycle(self.curVel)
            time.sleep(accelt/10)

    def stop(self):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        self.curVel = 0
        self.pwmPin.ChangeDutyCycle(self.curVel)

    def turn(self,degree):
        pass
        #code