

# ----------------------------------->  AutoMate WhatsApp through Web Browser

'''
# import lib

import pywhatkit
import time 

phn = '+923056754074'
msgs = 'Hello there is some msg'

# Get time in hour and minute

while True:
    tm = time.localtime(time.time()+80)
    hour = tm.tm_hour
    min = tm.tm_min
    
    pywhatkit.sendwhatmsg(phn, msgs, hour, min)
    time.sleep(10)
    
'''

print('Not Good Result')

#----------------------------------> AutoMate WhatsApp through PyAutoGui

'''

import pyautogui
import time

def send_msg(msg):
    pyautogui.typewrite(msg)
    time.sleep(0.1)
    pyautogui.press("enter")
# count = 0

while True:
    
    msgs = input('Enter Msg: ') # Here we can put our msg
    time.sleep(1)
    a = pyautogui.moveTo(x=439, y=739)
    clk = pyautogui.click(a)
    time.sleep(1)
    send_msg(msgs)


# these code help cursor to come input position

    a2 = pyautogui.moveTo(x=1119, y=624)
    cl = pyautogui.click(a2)

    
'''











