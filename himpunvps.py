import pyrebase
import httpx
import json
import time
import seting
import getlive
import random
import sys
import pytz
from datetime import datetime
from colorama import Fore, Style, init
init()

config = {
    "apiKey": "AIzaSyATkiylea79HwAQNoJHDa5XLCK6b7kK1Ys",
    "authDomain": "bling-1b0b0.firebaseapp.com",
    "databaseURL": "https://bling-1b0b0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "bling-1b0b0",
    "storageBucket": "bling-1b0b0.appspot.com",
    "messagingSenderId": "489126684041",
    "appId": "1:489126684041:web:0f6978ddf5f9b9929bed58"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()
persi = seting.versi()

def atoken():
    req = db.child('account').child('token').get()
    acc = req.val()["results"]
    return acc
def auid():
    uid = db.child('account').child('uid').get()
    acc = uid.val()["results"]
    return acc
dat = {"roomid": "0", 
"pake": [], 
"ganjilgenap": 2, 
"idroomarray": [], 
"iff": 1,
"jumtkn" : atoken()}


def tunggu(x):
    tz = pytz.timezone("Asia/Jakarta")
    print()
    while True:
        now = datetime.now(tz)
        jamm = now.strftime("%H:%M:%S")
        sys.stdout.write(f"  {jamm}/{x}   \r")
        sys.stdout.flush()
        detik = now.strftime("%S")
        if int(detik) == int(x):
            break
        time.sleep(0.5)


def c(colr, tex, dim):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,

            "BLACK": Fore.BLACK,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]}{tex}{Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]}{tex}{Style.RESET_ALL}"
    except:
        return tex




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
        req = httpx.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def getnum(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Game/GetTypeInfo"
    headers = {
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    query = {"game_type": "baijiale_1"}
    req = httpx.get(uri, params=query, headers=headers)
    ress = json.loads(req.text)
    try:
        return ress["result"]["current_round"]["number"]
    except:
        print("return error")


def betsic(x, type, num, gamevers, tbsoe):
    rType = {
        "big": "zonghe_da",
        "small": "zonghe_xiao",
        "odd": "zonghe_dan",
        "even": "zonghe_shuang",
        "any triple": "zonghe_weitou",
    }
    if tbsoe == 1:
        rType = {
            "player": "zonghe_da",
            "banker": "zonghe_xiao",
        }
    else:
        rType = {
            "player": "zonghe_dan",
            "banker": "zonghe_shuang",
        }

    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    rumnya = random.choice(dat["idroomarray"])
    # print(f'>>  {rumnya["nickname"]}')
    param = {
        "live_room_id": rumnya["live_id"],
        "game_type": "toubao_1",
        "game_sub": "zonghe",
        "game_number": gamevers,
        "detail": rType[type] + ":" + num + ";",
        "multiple": "1",
    }

    try:
        req = httpx.post(uri, data=json.dumps(param),
                         headers=headers, timeout=10)
        ress = json.loads(req.text)
        ress["result"]["room"] = rumnya["nickname"]
        return(ress)
    except Exception as e:
        print(f"Failed : {e}")
        return {"result": {'balance': '0.0', 'room': 'FAILED'}}


def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = httpx.get(uriweb, headers=headers)
    try:
        ress = json.loads(f.text)
        krm = [
            ress["result"]["nickname"],
            ress["result"]["balance"],
            ress["result"]["vip_name"],
            ress["result"]["id"],
        ]
        return krm
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


acc = auid()
print(f"jumlah semua token : {len(dat['jumtkn'])}")

# tokens = []
# token = jumtkn[aa:bb]
jedascan = 0.8  # float(input("jeda scan : "))
# print("filtering...")
# ikl = 1
# for i in token:
#     ceking = getinfo(i)
#     print(ceking)
#     if float(ceking[1]) >= 1.0:
#         tokens.append(i)
#     sys.stdout.write(f"\t {ikl} -> {len(tokens)}\r")
#     sys.stdout.flush()
#     ikl += 1
#     time.sleep(jedascan)

print()


def pilter():
    dat["pake"].clear()
    valuecoin = []
    # cek token ke 0 apakah ekpiret
    while True:
        if getinfo(dat["jumtkn"][0])[0] == "expiret":
            print()
            print("HARUS REFRES TOKEN")
            print()

            for sabar in range(7200, 0, -1):
                sys.stdout.write(f"{sabar}  lagi reset token \r")
                sys.stdout.flush()
                time.sleep(1)
            dat["jumtkn"]=atoken()
        else:
            break
    while True:
        turu=dat["jumtkn"][dat["iff"]-1:dat["iff"]][0]
        ceking = getinfo(turu)
        ceking.append(turu)
        # print(f"{ceking[1]} {ceking[0]}")
        jakun = 4
        if len(dat["pake"]) > jakun-1:
            print(f"\npick {jakun} akun")
            break
        else:
            if float(ceking[1]) >= 2.0:
                gngn = "Ganjil"
                gngnkey = "Ganjil"
                # print(
                #     f'coinnya = [{int(str(ceking[1].split(".")[0]))}]  {int(str(ceking[1].split(".")[0]))%2==0}')

                if int(str(ceking[1].split(".")[0])) % 2 == 0:  # genap
                    gngn = "Genap"
                if dat["ganjilgenap"] == 1:
                    gngnkey = "Genap"

                if ceking[4] not in dat["pake"]:
                    if gngnkey == "Genap" and gngn == "Genap":
                        dat["pake"].append(ceking[4])
                        print(
                            f"Add [{ceking[1]}] \t{ceking[0]} {gngn} -> {gngnkey}")
                        valuecoin.append(int(ceking[1].split(".")[0]))
                    if gngnkey == "Ganjil" and gngn == "Ganjil":
                        dat["pake"].append(ceking[4])
                        print(
                            f"Add [{ceking[1]}] \t{ceking[0]} {gngn} -> {gngnkey}")
                        valuecoin.append(int(ceking[1].split(".")[0]))
            else:
                dat["jumtkn"].pop(dat["jumtkn"].index(turu))
                # print(f"jumlah token : {len(tokens)}")

        sys.stdout.write(f"Scanning... {dat['iff']} -> {float(ceking[1])}            \r")
        sys.stdout.flush()
        dat["iff"] += 1
        if dat["iff"] > len(dat["jumtkn"]):
            dat["iff"] = 1
            break
        time.sleep(jedascan)
    return valuecoin


def represroom():
    print()
    print("  >> Refresh room")
    print()
    dat["idroomarray"] = getlive.roomall()
    return
def jammain():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%H%M")
    print(f"500>{jamm}<1900")
    if int(jamm)>500 and int(jamm)<1900:
        return True
    else:return False

hehe = ["player", "banker"]

represroom()
while True:
    if jammain():
        print("--------------- MAEN 5:00 > jam < 18:00")
        tunggu(11)
        try:
            # input("SCAN")
            if dat["ganjilgenap"] == 2:
                dat["ganjilgenap"] = 1
            else:
                dat["ganjilgenap"] = 2
            filtt = pilter()
            if len(filtt) % 2 == 1:
                filtt.pop(0)
                print("\npop : 0")
            if len(filtt) != 0:
                xkecil = min(filtt)
            else:
                xkecil = 1
            itrr = len(dat["pake"])
            print(f"<<<<<<<<<<<<<  {itrr} tokens Selected")
            if itrr == 1 or itrr == 0:
                if dat["ganjilgenap"] == 2:
                    dat["ganjilgenap"] = 1
                else:
                    dat["ganjilgenap"] = 2
                filtt = pilter()
                if len(filtt) % 2 == 1:
                    filtt.pop(0)
                    print("\npop : 0")
                if len(filtt) != 0:
                    xkecil = min(filtt)
                else:
                    xkecil = 1
                itrr = len(dat["pake"])
                print(f"<<<<<<<<<<<<<  {itrr} tokens Selected")
            if itrr % 2 != 0:
                dat["pake"].pop(0)

        except Exception as e:
            print(f"Error : {e}")
        itrr = len(dat["pake"])
        print(f">>>>>>>>>>>>> {itrr} akun Betting")
        if itrr == 0:
            print(f"Kosong ")
            print()
            for sabar in range(1900, 0, -1):
                sys.stdout.write(f"{sabar}   \r")
                sys.stdout.flush()
                time.sleep(1)
            represroom()
            # break

        else:
            # cari nilai terkecil
            print(f"terkecil = {xkecil}")

            tunggu(random.randint(25, 40))
            # input("BET")
            bett = str(xkecil)
            try:
                gamevers = getnum(dat["pake"][0])
            except Exception as e:
                print(f"ERROR : {e}")
            print(f"Game Version : {gamevers}")

            # print(json.dumps(dat["pake"], indent=2))
            jp, jb = [], []

            gasbet = {}
            for pola in range(itrr):
                if pola % 2 == 0:
                    type = 0
                else:
                    type = 1
                tkn = dat["pake"][pola]
                # untuk bet all in semuanya
                # bet(tkn, hehe[type], dataakun[itr][1].split('.')[0])
                # print(hehe[type], bett, gamevers)
                if hehe[type] == "banker":
                    dataa = {
                        "num": pola,
                        "tipe": hehe[type],
                        "tkn": tkn,
                        "jum": bett,
                        "verr": gamevers,
                        "warna": "red"
                    }
                    gasbet[pola] = (dataa)
                else:
                    dataa = {
                        "num": pola,
                        "tipe": hehe[type],
                        "tkn": tkn,
                        "jum": bett,
                        "verr": gamevers,
                        "warna": "blue"
                    }
                    gasbet[pola] = (dataa)

            lennya = len(gasbet)-1
            dahpick = []
            tipebsoe = random.choice([1, 2])
            while len(gasbet) != 0:
                # print(">>>>>>>>>>  "+str(len(gasbet)))
                while True:
                    badak = random.randint(0, lennya)
                    if badak not in dahpick:
                        dahpick.append(badak)
                        break

                dbt = gasbet[badak]
                # print()
                bettlol = betsic(dbt["tkn"], dbt["tipe"],
                                dbt["jum"], dbt["verr"], tipebsoe)
                # bettlol
                # {'msg': 'ok', 'code': 0, 'result': {'balance': '2.54', 'room': 'INDO: Kiewww'}}
                try:
                    if dbt["tipe"] == "player":
                        jp.append(
                            int("1"+str(bettlol["result"]["balance"].replace(".", ""))))
                    else:
                        jb.append(
                            int("1"+str(bettlol["result"]["balance"].replace(".", ""))))
                except:
                    jp.append("000")

                print(
                    c(dbt["warna"], f"{str(badak)} >> {str(bettlol['result'])}", 0))
                if bettlol["result"]["room"] == "FAILED":
                    if dat["ganjilgenap"] == 2:
                        dat["ganjilgenap"] = 1
                    else:
                        dat["ganjilgenap"] = 2
                    break

                del gasbet[badak]
                time.sleep(jedascan)

            try:
                apop = str(min(jb))
                apop = apop[1::]
                apop = (f"{apop[:1]}.{apop[1:5]}")
                bpop = str(min(jp))
                bpop = bpop[1::]
                bpop = (f"{bpop[:1]}.{bpop[1:5]}")

                print(c("blue", f"\tif player : {apop}", 0))
                print(c("red", f"\tif banker : {bpop}", 0))
            except:
                pass
    for sabar in range(1800, 0, -1):
        sys.stdout.write(f"{sabar} belum waktunya main  \r")
        sys.stdout.flush()
        time.sleep(1)
