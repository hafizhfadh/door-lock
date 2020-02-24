import requests

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
    if response['status']:
        print('Akses diterima ! %s' %response['message'])
    else:
        print('Akses ditolak ! %s' %response['message'])
