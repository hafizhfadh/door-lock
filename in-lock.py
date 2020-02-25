import requests
import os
import RPi.GPIO as GPIO
import signal
import sys

while True:
    GPIO.setmode(GPIO.BCM)
    pin.DOOR_SENSOR_PIN = 12
    URL = "http://api.wibs.sch.id//v2/dorm/post/outin.update-timestamp"
    rfid = input("Please insert RFID : ")
    data = {
        'student_rfid': rfid,
        'type': 'in'
    }
    r = requests.post(url=URL, data=data, headers={
        "Application-Token": "geSzgVahOlowulcgHEtQmu9Ybofk1lRnPFd3V5atSEu1SD1dt2"})
    response = r.json()
    if response['status']:
        print('Akses diterima ! %s' % response['message'])
        file = "granted.mp3"
        os.system("mpg123 " + file)
        GPIO.output(DOOR_SENSOR_PIN, False)
        GPIO.cleanup()
    else:
        print('Akses ditolak ! %s' % response['message'])
        file = "denied.mp3"
        os.system("mpg123 " + file)
        GPIO.output(DOOR_SENSOR_PIN, True)
        GPIO.cleanup()