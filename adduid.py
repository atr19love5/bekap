
import subprocess
import pyrebase
import json
config=json.loads(open("dbaddrs.json","r").read())
# config = {
#     "apiKey": "AIzaSyATkiylea79HwAQNoJHDa5XLCK6b7kK1Ys",
#     "authDomain": "bling-1b0b0.firebaseapp.com",
#     "databaseURL": "https://bling-1b0b0-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId": "bling-1b0b0",
#     "storageBucket": "bling-1b0b0.appspot.com",
#     "messagingSenderId": "489126684041",
#     "appId": "1:489126684041:web:0f6978ddf5f9b9929bed58"
# }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
patt = input("path packages : ")
patt = patt.replace("\\", "/")


while True:
    dbb = {"results": []}
    req = db.child('account').child('uid').child("results").get()
    acc = req.val()
    for tott in acc:
        dbb["results"].append(tott)

    # dbb["results"][1] = {"appsflyer_id": "1659116438820-1239098700765885385", "check_type": "0", "device_id": "Android_SM-J730F_com.dt01usera.ghjb_742E71268039A76A2011F34A2144F132",
    #                      "force_new": "2", "invite_code": "", "registration_id": "18071adc03cc524e255", "sign": "bf19ff6a5789fcd53fd2f8c9d2146098"}
    tet = 1
    for ppp in dbb["results"]:
        print(f'{tet}. {json.dumps(ppp)}')
        tet += 1

    print(f"total uid : {len(dbb['results'])}")

    nuid = json.loads(input("insert UID : "))
    dbb["results"].append(nuid)
    print(f"total uid : {len(dbb['results'])}")

    # print(json.dumps(dbb, indent=2))
    db.child("account").child("uid").update(dbb)
    if input("Press Enter to Delete Packages")=="":
        process = subprocess.Popen(['rm', '-rf', f'{patt}/packages'])
