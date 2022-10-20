import httpx,ambil,json,random

tkn=ambil.token()[0]

def getinfo(tkn,id):
    uriweb = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/UserInfo?show_id={id}&live_id="
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tkn,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = httpx.get(uriweb, headers=headers)
    ress = json.loads(f.text)["result"]["to"]
    print(json.dumps(ress,indent=2))

getinfo(tkn,input("id : "))