#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import signal
import sys
          
while True:  
    try:
          PIN_TRIGGER = 7
          PIN_ECHO = 11
          GPIO.setmode(GPIO.BOARD)
          GPIO.setup(PIN_TRIGGER, GPIO.OUT)
          GPIO.setup(PIN_ECHO, GPIO.IN)
          GPIO.output(PIN_TRIGGER, GPIO.LOW)

          #print ("Waiting for sensor to settle")

          time.sleep(0.5)

          #print ("Calculating distance")
    
          GPIO.output(PIN_TRIGGER, GPIO.HIGH)

          time.sleep(0.00001)

          GPIO.output(PIN_TRIGGER, GPIO.LOW)

          while GPIO.input(PIN_ECHO)==0:
                 pulse_start_time = time.time()
          while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

          pulse_duration = pulse_end_time - pulse_start_time
          distance = round(pulse_duration * 17150, 2)
          
          if (distance) < 100:
              print ("Distance detectada abaixo de 1m:",distance,"cm")
          #else:
              #print ('Distance acima de 1m')
      
    except KeyboardInterrupt:
        print ('erro')
        GPIO.cleanup()