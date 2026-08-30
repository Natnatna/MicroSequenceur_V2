from machine import Pin, ADC
import asyncio

#CORE
async def Run():
    await asyncio.gather(Input(), Line_sync(), Led_bpm(), Sync_in(), Sync_timer())

#SEQUENCEUR
async def Sequenceur():
    await asyncio.gather(Un_temp(), Demi_temp(), Quart_temp())

async def Line_sync():
    while 1 == 1:
        for position_line in range(8):
            line = index_line[position_line]
            line.value(1)
            await Sequenceur()
            line.value(0)

async def Un_temp():
    un_temp_1.value(1)
    await asyncio.sleep(bpm-attack)
    un_temp_1.value(0)
    await asyncio.sleep(attack)

async def Demi_temp():
    for position_demi_temp in range(2):
        demi_temp = index_demi_temp[position_demi_temp]
        demi_temp.value(1)
        await asyncio.sleep((bpm/2)-(attack/2))
        demi_temp.value(0)
        await asyncio.sleep(attack/2)

async def Quart_temp():
    for position_temp in range(4):
        temp = index_quart_temp[position_temp]
        temp.value(1)
        await asyncio.sleep(round((bpm/4)-(attack/4), 2))
        temp.value(0)
        await asyncio.sleep(attack/4)

#CONTRÔLS 
async def Input():
    global attack
    global bpm
    while 1 == 1:
        init_bpm = int(ADC(pin_value_bpm).read_u16()/1000)
        bpm = round(1/(list_bpm[init_bpm]/60), 2)
        init_attack = int(ADC(pin_value_attack).read_u16()/1000)
        attack = round(init_attack*0.01, 2)
        await asyncio.sleep_ms(1)

###SYNC OPTIONS
#0,5v en input ou output
#une puls toutes les deux notes ou deux puls par temp 

###SYNC IN
async def Sync_in():
    #definir le compteur  selon le temp
    global x
    x = 0
    while 1 == 1:
        sync_in = pin_sync_in.value()
        if sync_in == 1:
            x += 1
        vsync = sync_in
        while vsync == sync_in:
            await asyncio.sleep(0.01)
            sync_in = pin_sync_in.value()

async def Sync_timer():
    global x
    while 1 == 1:
        await asyncio.sleep(3)
        bpm_in = (x//6)*60
        print(bpm_in, "bpm en input   ")
        x = 0

###SYNC OUT
async def Sync_out():
    while 1 == 1:
        pin_sync_out.value(1)
        await asyncio.sleep(bpm/4)
        pin_sync_out.value(0)
        await asyncio.sleep(bpm/4)

#Indicateur BPM
async def Led_bpm():
    while 1 == 1:
        led_bpm.value(1)
        await asyncio.sleep(bpm/2)
        led_bpm.value(0)
        await asyncio.sleep(bpm/2)


###INIT###

#LED indicateur power on
LED = Pin(25, Pin.OUT)

LED.value(1)

#init SYNC IN
pin_sync_in = Pin(16, Pin.IN)

#init SYNC OUT
pin_sync_out = Pin(18, Pin.OUT)

#init LED BPM
led_bpm = Pin(17, Pin.OUT)

#init BPM
pin_value_bpm = 28
list_bpm = []
for index_bpm in range(60, 256, 3):
    list_bpm.append(index_bpm)

#init ATTACK
pin_value_attack = 27

#init LINE
line_1 = Pin(6, Pin.OUT)
line_2 = Pin(7, Pin.OUT)
line_3 = Pin(8, Pin.OUT)
line_4 = Pin(9, Pin.OUT)
line_5 = Pin(10, Pin.OUT)
line_6 = Pin(11, Pin.OUT)
line_7 = Pin(12, Pin.OUT)
line_8 = Pin(13, Pin.OUT)
index_line = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8]

# init 1/1T
un_temp_1 = Pin(14, Pin.OUT)

#init 1/2T
demi_temp_1 = Pin(0, Pin.OUT)
demi_temp_2 = Pin(1, Pin.OUT)
index_demi_temp = [demi_temp_1, demi_temp_2]

#init 1/4T
quart_temp_1 = Pin(2, Pin.OUT)
quart_temp_2 = Pin(3, Pin.OUT)
quart_temp_3 = Pin(4, Pin.OUT)
quart_temp_4 = Pin(5, Pin.OUT)
index_quart_temp = [quart_temp_1, quart_temp_2, quart_temp_3, quart_temp_4]


###RUN###
asyncio.run(Run())
