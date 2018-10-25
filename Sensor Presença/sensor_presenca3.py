import RPi.GPIO as GPIO
import time
import signal
import sys
          
while True:  
    try:
          PIN_TRIGGER1 = 7
          PIN_ECHO1 = 11
          PIN_TRIGGER2 = 18
          PIN_ECHO2 = 24
          GPIO.setmode(GPIO.BOARD)
          
          GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
          GPIO.setup(PIN_ECHO1, GPIO.IN)
          GPIO.output(PIN_TRIGGER1, GPIO.LOW)
          
          GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
          GPIO.setup(PIN_ECHO2, GPIO.IN)
          GPIO.output(PIN_TRIGGER2, GPIO.LOW)

          #print ("Waiting for sensor to settle")

          time.sleep(0.5)

          #print ("Calculating distance")
    
          GPIO.output(PIN_TRIGGER1, GPIO.HIGH)
          GPIO.output(PIN_TRIGGER2, GPIO.HIGH)

          time.sleep(0.00001)

          GPIO.output(PIN_TRIGGER1, GPIO.LOW)
          GPIO.output(PIN_TRIGGER2, GPIO.LOW)

          while GPIO.input(PIN_ECHO1)==0:
                 pulse_start_time1 = time.time()
                 
          while GPIO.input(PIN_ECHO2)==0:
                 pulse_start_time2 = time.time()
                 
          while GPIO.input(PIN_ECHO1)==1:
                pulse_end_time1 = time.time()
                
          while GPIO.input(PIN_ECHO2)==1:
                pulse_end_time2 = time.time()
                
          pulse_duration1 = pulse_end_time1 - pulse_start_time1
          distance1 = round(pulse_duration1 * 17150, 2)
          
          pulse_duration2 = pulse_end_time2 - pulse_start_time2
          distance2 = round(pulse_duration2 * 17150, 2)
          
          if (distance1) < 100 or (distance2) < 100:
              print ("Distance detectada abaixo de 1m:",distance1,"cm")
          #else:
              #print ('Distance acima de 1m')
      
    except KeyboardInterrupt:
        print ('erro')
        GPIO.cleanup()