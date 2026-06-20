import asyncio
from machine import Pin, ADC

async def Test():
    while 1 == 1:
        test = round((bpm+attack), 2)-attack == bpm
        print(bpm, attack, (round(bpm+attack))-attack, test)
        await asyncio.sleep_ms(100)
#Core
async def main():
    await asyncio.gather(Input(), Sequenceur(), Led_bpm(), Test())

#Inputs
async def Input():
    global attack
    global bpm
    while 1 == 1:
        init_bpm = int(ADC(pin_value_bpm).read_u16()/1000)
        bpm = round(1/(list_bpm[init_bpm]/60), 2)
        init_attack = int(ADC(pin_value_attack).read_u16()/1000)
        attack = round(init_attack*0.01, 2)
        await asyncio.sleep_ms(1)

########################################################################
###Fonctions Sequenceur
########################################################################
async def Sequenceur():
    await asyncio.gather(Line(), Demi_temp(), Quart_temp())

async def Line():
    while 1 == 1:
        for position_line in range(8):
            line = index_line[position_line]
            line.value(1)
            await asyncio.sleep(round(bpm-attack, 2))
            line.value(0)
            await asyncio.sleep(attack)

async def Demi_temp():
    while 1 == 1:
        for position_demi_temp in range(2):
            demi_temp = index_demi_temp[position_demi_temp]
            demi_temp.value(1)
            await asyncio.sleep((bpm/2)-(attack/2))
            demi_temp.value(0)
            await asyncio.sleep(attack/2)

async def Quart_temp():
    global position_temp
    while 1 == 1:
        for position_temp in range(4):
            temp = index_quart_temp[position_temp]
            temp.value(1)
            await asyncio.sleep(round((bpm/4)-(attack/4), 2))
            temp.value(0)
            await asyncio.sleep(attack/4)

##########################################################################
async def Led_bpm():
    while 1 == 1:
        led_bpm.value(1)
        await asyncio.sleep(bpm/2)
        led_bpm.value(0)
        await asyncio.sleep(bpm/2)
                
##########################################################################
###Initialisations
##########################################################################
#initialisation BPM
pin_value_bpm = 28
list_bpm = []
for index_bpm in range(60, 260, 3):
    list_bpm.append(index_bpm)

#initialisation ATTACK
pin_value_attack = 27


#initialisation Sequenceur
#1/1t
line_1 = Pin(6, Pin.OUT)
line_2 = Pin(7, Pin.OUT)
line_3 = Pin(8, Pin.OUT)
line_4 = Pin(9, Pin.OUT)
line_5 = Pin(10, Pin.OUT)
line_6 = Pin(11, Pin.OUT)
line_7 = Pin(12, Pin.OUT)
line_8 = Pin(13, Pin.OUT)

index_line = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8]


#1/2t
demi_temp_1 = Pin(0, Pin.OUT)
demi_temp_2 = Pin(1, Pin.OUT)

index_demi_temp = [demi_temp_1, demi_temp_2]


#1/4t
quart_temp_1 = Pin(2, Pin.OUT)
quart_temp_2 = Pin(3, Pin.OUT)
quart_temp_3 = Pin(4, Pin.OUT)
quart_temp_4 = Pin(5, Pin.OUT)

index_quart_temp = [quart_temp_1, quart_temp_2, quart_temp_3, quart_temp_4]


#LED BPM initialisation
led_bpm = Pin(15, Pin.OUT)


##############################################################
###debut du programe
##############################################################
asyncio.run(main())
