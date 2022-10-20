import requests,random
import seting
import json


#type 3 = login
#type 4 = bind

def getcode(tkn, email, sign,tkncode):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/GetEmailCode"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.1{random.randint(11111,99999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "x-token": tkn,
        "Accept-Encoding": "identity",
        "X-Version": seting.versi(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "type": 4,
        "email": email,
        "sign": sign,
        "token":tkncode
    }

    try:
        req = requests.post(uri, data=param, headers=headers)
        ress = json.loads(req.text)
        return ress["msg"]
    except Exception as e:
        print("Failed : "+str(e))
        return 0
