#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(26, gpio.IN)

while True:
	if(gpio.input(26) == 1):
		print('Botão pressionado')
	else:
		print('Botao desligado')
	
	time.sleep(0.5)

gpio.cleanup()
exit()