import RPi.GPIO as gp
import subprocess
import time
import os

BUTTON_ONE = 6
BUTTON_TWO = 13
BUTTON_THREE = 19
BUTTON_FOUR = 26
ENTER_BUTTON = 5

passphrase = "1123"

gp.setmode(gp.BCM)
gp.setup(4, gp.OUT) ## logout warning light
gp.setup(BUTTON_ONE, gp.IN)
gp.setup(BUTTON_TWO, gp.IN)
gp.setup(BUTTON_THREE, gp.IN)
gp.setup(BUTTON_FOUR, gp.IN)
gp.setup(ENTER_BUTTON, gp.IN)

def button_decode() -> str:
    if gp.input(BUTTON_ONE):
        while(gp.input(BUTTON_ONE)):
            continue
        return "1"
    elif gp.input(BUTTON_TWO):
        while(gp.input(BUTTON_TWO)):
            continue
        return "2"
    elif gp.input(BUTTON_THREE):
        while(gp.input(BUTTON_THREE)):
            continue
        return "3"
    elif gp.input(BUTTON_FOUR):
        while(gp.input(BUTTON_FOUR)):
            continue
        return "4"
    else:
        return ""
    
try:
    while True:
        current_passphrase = ""
        print('please enter password')
        while not gp.input(ENTER_BUTTON):
            current_passphrase += button_decode()
        time.sleep(.1)
        while(gp.input(ENTER_BUTTON)):
            time.sleep(.1)
        print(current_passphrase)
        if(current_passphrase == passphrase): #change arg 2 to your untrusted PC user ssh password // hardcoded user andd ip but can be changed to be modular
            permission = subprocess.run(["openssl", "dgst", "-sha256", "-sign", "private_key.pem", "-out", "sig.bin", "sig"])
            subprocess.run(["sshpass","-p", "password", "scp", "sig", "aisquaisqu@192.168.1.152:/Users/aisquaisqu/piproject/root"])
            subprocess.run(["sshpass","-p", "password", "scp", "sig.bin", "aisquaisqu@192.168.1.152:/Users/aisquaisqu/piproject/root"])
            os.remove("sig.bin")
            print("sig sent")

finally:
    gp.cleanup()

        


   