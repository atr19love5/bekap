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
        req = requests.post(uri, data=json.dumps(param), headers=headers,timeout=10)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        ress = {"result":{
            "nickname":str(e),
            "balance":"0",
            "vip_name":"0",
            "show_id":"0",
            "access_token":"0",
            }}
        return ress
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

ataroinvcode = ""
base={}
jeda=float(5.0)

def cekreset():
    for itr in range(itrawal,len(base['acc']),1):
        try:
            tokenakun=base['token'][itr]
            cekakun=getinfo(tokenakun)
        except Exception as e:
            cekakun=['expiret','expiret','expiret','expiret']
        if cekakun[3] == "expiret":
            for x in range(random.randint(jeda,jeda+10),0,-1):
                sys.stdout.write(f"  {x}   \r")
                sys.stdout.flush()
                time.sleep(1)
            print(f"______________[ login ]_______________[{itr}]")
            while True:
                refreshtkn = loginid(db.child('account').child('uid').child('results').child(itr).get().val())
                # print(refreshtkn)
                if refreshtkn["code"] == 0:
                    bnama,bkoin,bvip,vid=refreshtkn["result"]["nickname"],refreshtkn["result"]["balance"],refreshtkn["result"]["vip_name"],refreshtkn["result"]["show_id"]
                    dissp=[bnama,bkoin,bvip,vid]
                    print(f'{dissp}')
                    tokenbaru = refreshtkn["result"]["access_token"]
                    db.child('account').child('token').child('results').update({itr:tokenbaru})
                    break
                else:
                    print(refreshtkn["msg"])
                time.sleep(5)
        else:
            for x in range(2,0,-1):
                sys.stdout.write(f"  {x}   \r")
                sys.stdout.flush()
                time.sleep(1)
            print(f"______________[ aman ]________________[{itr}]")
            print(cekakun)


def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%m/%d/%Y, %H:%M:%S")
    minut = now.strftime("%M")
    secc = now.strftime("%S")
    if int(minut)%30==0 and int(minut)!=0 and secc=="00":
        print("???>> "+str(jamm))
        return True
    else:
        sys.stdout.write(f"  {jamm}  \r")
        sys.stdout.flush()
        return False

try:
    tes=True
    itrawal=int(sys.argv[1])
    print("TEEEEEEEEES")
except:
    tes=False
    itrawal=0
#tes py autoreset.py tokenawal
#normal py autoreset.py
while True:
    if jam() or tes:
        print("???>> Melakukan Cek Token")
        base["token"]=ambil.token()
        base["acc"]=ambil.uid()
        print(f"jumlah uid : {len(base['acc'])}")
        cekreset()
        print("???>> Selesai Cek\n")
    time.sleep(1)


