import requests
import os
import RPi.GPIO as GPIO

while True:
    CONTROL_PIN = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CONTROL_PIN, GPIO.OUT)
    GPIO.output(CONTROL_PIN, True)
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
        GPIO.output(CONTROL_PIN, False)
        GPIO.cleanup()
    else:
        print('Akses ditolak ! %s' % response['message'])
        # file = "denied.mp3"
        # os.system("mpg123 " + file)
        GPIO.output(CONTROL_PIN, True)
        GPIO.cleanup()
