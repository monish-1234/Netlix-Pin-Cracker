from pynput.keyboard import Controller #Importing "pynput" module for simultaing key press
import time



time.sleep(2)
keyboard=Controller()

for x in range(0000,2000):
    pin=str(x)
    pin=pin.zfill(4)
    pin=list(pin)
    
    keyboard.press(pin[0]) #First pin key press - start
    keyboard.release(pin[0]) #First pin key press - end 
    time.sleep(0.1)
    
    keyboard.press(pin[1]) #Second pin key press - start
    keyboard.release(pin[1]) #Second pin key press - end 
    time.sleep(0.1)
    
    keyboard.press(pin[2]) #Third pin  key press - start
    keyboard.release(pin[2]) #Third pin key press - end  
    time.sleep(0.1)
    
    keyboard.press(pin[3]) #Fourth pin key press - start
    keyboard.release(pin[3]) #Fourth pin key press - end
    time.sleep(0.1)
    print(pin)
     


