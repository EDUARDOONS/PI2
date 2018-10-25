import RPi.GPIO as GPIO
import time

BtnPin1 = 16    # pin18 --- fim_curso1
BtnPin2 = 22    # pin22 --- fim_curso2

GPIO.setmode(GPIO.BOARD)       # Pinagem física
GPIO.setup(BtnPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Pino do botão como saída e aciona o pull-up
GPIO.setup(BtnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

out1 = False
out2 = False

# Funcao de callback para botao 1
def callback_bt_1(channel):
    global out1
    print('Porta fechada')
    #out1 = not out1
    #GPIO.output(LedPin1, out1)

# Funcao de callback para botao 2
def callback_bt_2(channel):
    global out2
    print('Porta aberta')
    out2 = not out2
    #GPIO.output(LedPin2, out2)

# Registra funcoes de callback
GPIO.add_event_detect(BtnPin1, GPIO.RISING, callback=callback_bt_1, bouncetime=200)
GPIO.add_event_detect(BtnPin2, GPIO.RISING, callback=callback_bt_2, bouncetime=200)

# Loop principal
print('Pressione Ctrl+C para sair')
try:
    while True:
        
        if out1 == True and out2 == True:
            print('Porta em Movimento')
            
        time.sleep(0.5)
except KeyboardInterrupt:
    # Ctrl+C foi pressionado
    pass
 
#GPIO.output([LedPin1, LedPin2], 0)
GPIO.cleanup()  # Limpa configuração
