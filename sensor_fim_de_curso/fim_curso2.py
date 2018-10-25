import RPi.GPIO as GPIO
import time

BtnPin1 = 22    # pin3 --- fim_curso1
BtnPin2 = 16    # pin3 --- fim_curso2
Rele = 12
Sensor = 37

GPIO.setmode(GPIO.BOARD)
 
 #Define o pino do botao como entrada
GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BtnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Sensor, GPIO.IN)

#Aciona o Relay
GPIO.setup(Rele, GPIO.OUT)

try:
    while True:
    #Verifica se o botao foi pressionado
        if GPIO.input(Sensor) == True:
            print('Sensor acionado')
        if GPIO.input(BtnPin1) == True:
            #Incrementa a variavel contador
            print('Porta fechada')
            GPIO.output(Rele,1)
        elif GPIO.input(BtnPin1) == False and GPIO.input(BtnPin2) == False:
            print('Porta em movimento')
            
        elif GPIO.input(BtnPin2) == True:
            GPIO.output(Rele,0)
            print('Porta aberta')
  
        
except KeyboardInterrupt:
    # Ctrl+C foi pressionado
        pass
 
#GPIO.output([LedPin1, LedPin2], 0)
GPIO.cleanup()  # Limpa configuração