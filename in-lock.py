import requests
from num2words import num2words
from subprocess import call

while True:
    URL = "http://api.wibs.sch.id//v2/dorm/post/outin.update-timestamp"
    rfid = input("Please insert RFID :")
    data = {
        'student_rfid': rfid,
        'type': 'in'
    }
    r = requests.post(url=URL, data=data, headers={
        "Application-Token": "geSzgVahOlowulcgHEtQmu9Ybofk1lRnPFd3V5atSEu1SD1dt2"})
    response = r.json()
    cmd_beg = 'espeak '
    # To play back the stored .wav file and to dump the std errors to /dev/null
    cmd_end = ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null'
    cmd_out = '--stdout > /home/pi/Desktop/Text.wav '  # To store the voice file
   if response['status']:
        print('Akses diterima ! %s' % response['message'])
        call([cmd_beg+cmd_out+"Access_Granted"+cmd_end], shell=True)
    else:
        print('Akses ditolak ! %s' % response['message'])
        call([cmd_beg+cmd_out+"Access_Denied"+cmd_end], shell=True)
