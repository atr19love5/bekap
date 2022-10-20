import json
from collections import OrderedDict
import datetime
import pyrebase
import pytz


config=json.loads(open("dbaddrs.json","r").read())


firebase = pyrebase.initialize_app(config)
db = firebase.database()


def getdurasi(x1):
    now = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
    s1 = (now.strftime("%H%M"))
    ss1 = datetime.datetime.strptime(s1, "%H%M")
    # print(ss1)

    dttr = x1
    tes = datetime.datetime.strptime(dttr, '%H:%M')
    s2 = (tes.strftime("%H%M"))
    ss2 = datetime.datetime.strptime(s2, "%H%M")
    # print(ss2)

    return(ss1-ss2)


dt = db.child('host').get()
chil = []
x = 0
for t in dt:
    x += 1
    nama = t.val()["nickname"]
    chil.append(nama)
    print(f"{x}. {nama}")

while True:
    print()
    inp = input("room nomor : ")
    cil = chil[int(inp) - 1]
    getrum = db.child('host').child(cil).get()
    rum = getrum.val()

    duras = getdurasi(rum["jamlive"][:5])
    for tt in rum:
        print(f"\t{tt} : {rum[tt]}")
    print(f"\tDurasi : {duras}")
