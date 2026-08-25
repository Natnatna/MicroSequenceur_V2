#TEST sur une line mode semi-réel
#doit donnée 12v si circuit ferméer
#doit donnée 0v si circuit ouvert
#doit donnée 12v si sw_x ferméer et que un sw_t feméer d'une durée en fonction du Temp choisit
#doit donnée 0v si sw_x ouvert et que n'importe quelle sw_t ferméer
from machine import Pin
import time

#line a tester
line = Pin(6, Pin.OUT)

un_temp_1 = Pin(14, Pin.OUT)
demi_temp_1 = Pin(0, Pin.OUT)
demi_temp_2 = Pin(1, Pin.OUT)
quart_temp_1 = Pin(2, Pin.OUT)
quart_temp_2 = Pin(3, Pin.OUT)
quart_temp_3 = Pin(4, Pin.OUT)
quart_temp_4 = Pin(5, Pin.OUT)

line.value(1)
while 1 == 1:
    un_temp_1.value(1)
    demi_temp_1.value(1)
    quart_temp_1.value(1)
    time.sleep(1)

#1/4
    quart_temp_1.value(0)
    quart_temp_2.value(1)
    time.sleep(1)

#2/4
    demi_temp_1.value(0)
    demi_temp_2.value(1)
    quart_temp_2.value(0)
    quart_temp_3.value(1)
    time.sleep(1)

#3/4
    quart_temp_3.value(0)
    quart_temp_4.value(1)
    time.sleep(1)

#4/4
    demi_temp_2.value(0)
    quart_temp_4.value(0)
    un_temp_1.value(0)
