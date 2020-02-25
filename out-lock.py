import requests
import os
import RPi.GPIO as GPIO
import time

def setDoorStatus(status, response):
    if status:
        print('Akses diterima ! %s' % response['message'])
        # file = "granted.mp3"
        # os.system("mpg123 " + file)
        GPIO.output(CONTROL_PIN, False)
        time.sleep(10)
        GPIO.output(CONTROL_PIN, True)
    else:
        print('Akses ditolak ! %s' % response['message'])
        # file = "denied.mp3"
        # os.system("mpg123 " + file)
        GPIO.output(CONTROL_PIN, True)

def sendData(rfid):
    URL = "http://api.wibs.sch.id//v2/dorm/post/outin.update-timestamp"
    data = {
        'student_rfid': rfid,
        'type': 'out'
    }
    r = requests.post(url=URL, data=data, headers={
            "Application-Token": "geSzgVahOlowulcgHEtQmu9Ybofk1lRnPFd3V5atSEu1SD1dt2"})
    response = r.json()
    setDoorStatus(status = response['status'], response = response)

while True:
    try:
        CONTROL_PIN = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(CONTROL_PIN, GPIO.OUT)
        GPIO.output(CONTROL_PIN, True)
        rfid = input("Please insert RFID : ")
        sendData(rfid = rfid)
        GPIO.cleanup()
    finally:
        GPIO.output(CONTROL_PIN, True)
        GPIO.cleanup()
