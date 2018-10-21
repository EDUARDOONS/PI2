import RPi.GPIO as GPIO    #Importamos a libraria GPIO
import time
#Importamos time (time.sleep)
GPIO.setmode(GPIO.BCM)     #Colocamos a placa em modo BCM
GPIO_TRIGGER = 7          #Usamos o pin GPIO 25 como TRIGGER
GPIO_ECHO    = 11           #Usamos o pin GPIO 7 como ECHO
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Configuramos Trigger como saída
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Configuramos Echo como entrada
GPIO.output(GPIO_TRIGGER,False)    #Colocamos o pin 25 como LOW
 
 
try:
    while True:     #Iniciamos un loop infinito
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos uma pressão de ultrasonidos
        time.sleep(0.00001)              #Uma pequena pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos a pressão
        start = time.time()              #Guarda o tempo atual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Enquanto o sensor não receba sinal...
            start = time.time()          #Mantemos o tempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Se o sensor recebe sinal...
            stop = time.time()           #Guarda o tempo actual mediante time.time() noutra variavel
        elapsed = stop-start             #Obtemos o tempo decorrido entre envío y receção
        distance = (elapsed * 34300)/2   #Distancia é igual ao tempo por velocidade partido por 2   D = (T x V)/2
        print (distance)                   #Devolvemos a distancia (em centímetros) por ecrã
        time.sleep(1)                    #Pequena pausa para não saturar o procesador do Raspberry
except KeyboardInterrupt:                #Se o utilizador pressionar CONTROL+C...
    print ("quit")                         #Avisamos do encerramento ao utilizaador
    GPIO.cleanup()   