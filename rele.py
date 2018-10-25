import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

try: 
while (True):
 
    if(GPIO.input(15) == 1):
       
       GPIO.output(12,0)
 
    else:
  
       GPIO.output(12,1)
except KeyboardInterrupt:
    # Ctrl+C foi pressionado
        pass
 
GPIO.cleanup()  # Limpa configuração