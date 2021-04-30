# Netflix Profile Pin Cracker

Brute force Netflix Profile Pin.

Note: This does not crack Netflix account passwords. This is only useful for cracking Profile Pin After Login.

## Dependencies

This Script Uses Pynput to mimic Keyboard Inputs. So install pynput by running the following command

```bash
pip install pynput
```

## Usage

1. Download ZIP/ Clone the repo to your Personal Computer.
2. Open Command Prompt in the script folder
3. run the command provided below

```bash
python start.py
```
4. Within 7 seconds Click on the Enter Pin box in Netflix. 

![image](https://user-images.githubusercontent.com/26372820/116726446-e85c0a00-aa00-11eb-9f61-de658b156b2c.png)


## Recommended Usage

This script calls keyboard keys from 0000 to 9999.

Run the program and immediately click on the first pin box.

This script can check 2 pins in a second. 

Thus meaning it would take 84 minutes to check from 0000 to 9999 pins. Hope that the pin doesn't start with 9 XD

After Netlix loads, Immediately stop the program and modify the 0000 and 9999 in 

```python
for x in range(0000,9999):
```
to 

0000 to the last number printed minus 100

9999 to the last number printed

and increase the sleep time in 

```python
keyboard.release(pin[3]) #Fourth pin key press - end
    time.sleep(0.1)
```

to 
```python
keyboard.release(pin[3]) #Fourth pin key press - end
    time.sleep(2)
```

So that the script runs slowly giving you time to find the exact pin

## Disclaimer

The Author/I am not responsible in any way if this script is used for malicious purposes.

Please use this only for the intended purpose,that is....messing with your friends

