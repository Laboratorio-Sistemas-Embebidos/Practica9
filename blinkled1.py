import RPi.GPIO as GPIO
from time import sleep

def peripheral_setup():
 GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
 global led1
 led1 = 4  #si cambiar de BCM a Board defina el número del pin acorde a los pines de la raspberry
 GPIO.setup(led1, GPIO.OUT)
 
def peripheral_loop():
 GPIO.output(led1,True)
 sleep(2)
 GPIO.output(led1,False)
 sleep(2)

# Main function
def main () :

# Setup
 peripheral_setup()

# Infinite loop
 while 1 :
  peripheral_loop()
  pass

# Command line execution #asumir sera llamado desde la consola, no desde otro archivo py
if __name__ == '__main__' :
   main()

