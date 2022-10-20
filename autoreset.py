import requests
import json
import time
import pytz
import seting,random
import sys
from datetime import datetime
import ambil

import pyrebase

config=json.loads(open("dbaddrs.json","r").read())


firebase = pyrebase.initialize_app(config)
db = firebase.database()
persi = seting.versi()

def tokensatu(tknke):
    req = db.child('account').child('token').child('results').child(tknke).get()
    acc = req.val()
    return acc

def loginid(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_LoginRegister/Login"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = x
    # kalau mau reset v1
    # param['force_new'] = '1'
    # print(param)
    # exit()

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0
def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    stat=0
    while stat!=200:
        f = requests.get(uriweb, headers=headers)
        stat=f.status_code
        if stat==200:
            ress = json.loads(f.text)
            try:
                krm = [
                    ress["result"]["nickname"],
                    ress["result"]["balance"],
                    ress["result"]["vip_name"],
                    ress["result"]["id"],
                ]
                return krm
            except:
                krm = [
                    x[-4:],
                    0.0,
                    str(ress['msg']),
                    "expiret",
                ]
        else:
            print("Reconnect")
    return krm

ataroinvcode = "yBooNa"
acc = ambil.uid()
print(f"\njumlah uid : {len(acc)}")
print("0 juga termasuk")
lpp=input("Enter To All")
if lpp=="":
    tkn1,tkn2=0,len(acc)
else:
    tkn1,tkn2=int(input("tkn1 : ")),int(input("tkn2 : "))
jeda=float(input("waktu jeda : "))
token=ambil.token()

def reset():
    itr = tkn1
    for id in acc[tkn1:tkn2]:
        while True:
            print(f"___________________________________[{itr}]")

            tkn = loginid(id)
            if tkn!=0:
                if tkn["code"] == 0:
                    print(tkn)
                    tknn = tkn["result"]["access_token"]
                    db.child('account').child('token').child('results').update({itr:tknn})
                    itr += 1
                        
                    for x in range(random.randint(jeda,jeda+10),0,-1):
                        sys.stdout.write(f"  {x}   \r")
                        sys.stdout.flush()
                        time.sleep(1)
                    break
            else:
                print(f"  [{itr}]  request eror : {tkn}")
                for i in range(random.randint(jeda,jeda+10)):
                    sys.stdout.write(f"{itr}\r")
                    sys.stdout.flush()
                    time.sleep(1)

try:
    sys.argv[1]
    tes = True
    print("Tes mode")
except:
    tes = False
jamar = []


def jam(cektkn):
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%m/%d/%Y, %H:%M")
    minut = now.strftime("%H%M")
    xxx=getinfo(cektkn)
    print(xxx)
    if xxx[2]=="The account has been logged in to other devices":
        jamar.append(str(jamm))
        print("•>> "+str(jamm))
        return True
    else:
        # print(""+str(jamm))
        return False
    # if minut == "0730" and jamm not in jamar:
    #     jamar.append(str(jamm))
    #     print("•>> "+str(jamm))
    #     return True
    # else:
    #     # print(""+str(jamm))
    #     return False


resetdong = False
tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
jamm = now.strftime("%m/%d/%Y, %H:%M")
print(jamm)
while True:
    jlk = jam(tokensatu(random.randint(0,100)))
    if tes == True:
        tes = False
        jlk = True
    if jlk == False:
        pass
    else:
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        klj = now.strftime("%m/%d/%Y, %H:%M")

        resetdong = False
        print("•>> Melakukan Reset Token")
        reset()
        print("•>> Selesai Reset")

    for x in range(60,0,-1):
        sys.stdout.write(f"  {x}   \r")
        sys.stdout.flush()
        time.sleep(1)
