import requests
import os
import RPi.GPIO as GPIO
import time
import logging

#This function switches on the relay on or off and expects the argument 'on' or 'off'

def relay_manual(action):
    # Selecting which GPIO to target
    GPIO_CONTROL = 18
    if action == "on":
        # We will be using the BCM GPIO numbering
        GPIO.setmode(GPIO.BCM)
        # Set CONTROL to OUTPUT mode
        GPIO.setup(GPIO_CONTROL, GPIO.OUT)
        #Starting the relay
        GPIO.output(GPIO_CONTROL, True)
        #Logging the event
        logging.basicConfig(format='%(asctime)s %(message)s',
                            filename='/home/pi/logging/events.log', level=logging.INFO)
        logging.info('Relay has been manually switched on, from out-lock.py')
    elif action == "off":
        try:
            #Stopping the relay
            GPIO.output(GPIO_CONTROL, False)
        except:
            # We will be using the BCM GPIO numbering
            GPIO.setmode(GPIO.BCM)
            # Set CONTROL to OUTPUT mode
            GPIO.setup(GPIO_CONTROL, GPIO.OUT)
            #Starting the relay
            GPIO.output(GPIO_CONTROL, False)
        #Logging the event
        logging.basicConfig(format='%(asctime)s %(message)s',
                            filename='/home/pi/logging/events.log', level=logging.INFO)
        logging.info('Relay has been manually switched off, from out-lock.py')
        #Cleanup
        GPIO.cleanup()

while True:
    try:
        relay_manual("on")
        URL = "http://api.wibs.sch.id//v2/dorm/post/outin.update-timestamp"
        rfid = input("Please insert RFID : ")
        data = {
            'student_rfid': rfid,
            'type': 'out'
        }
        r = requests.post(url=URL, data=data, headers={
            "Application-Token": "geSzgVahOlowulcgHEtQmu9Ybofk1lRnPFd3V5atSEu1SD1dt2"})
        response = r.json()
        if response['status']:
            print('Akses diterima ! %s' % response['message'])
            # file = "granted.mp3"
            # os.system("mpg123 " + file)
            relay_manual("off")
            time.sleep(10)
        else:
            print('Akses ditolak ! %s' % response['message'])
            # file = "denied.mp3"
            # os.system("mpg123 " + file)
            relay_manual("on")
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
