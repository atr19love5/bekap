import getapi
import pyrebase,json
config=json.loads(open("dbaddrs.json","r").read())

firebase = pyrebase.initialize_app(config)
db = firebase.database()


while True:
    # dbb = {"results": []}
    # req = db.child('yoha').child('akun').child("results").get()
    # acc = req.val()
    # for tott in acc:
    #     dbb["results"].append(tott)

    # tet = 1
    # for ppp in dbb["results"]:
    #     print(f'  {tet}. {ppp["no"]}')
    #     tet += 1
    # print(f"  total uid : {len(dbb['results'])}")
    inpp=input("input? q to exit")
    nomer = input("\tnomor send code : ")
    if nomer.startswith("0"):
        print("auto change 0 to 62")
        nomer = "62"+nomer[1:]
    print(nomer)
    
    if inpp!="q":
        getapi.sendcode(nomer)
        
    passwd = "Hanzo123"
    vcode = input("code : ")
    getapi.registernodb(nomer, passwd, vcode)

    # passwd = "t4ufiq654321"
    # vcode = input("code : ")
    # print(getapi.register(nomer, passwd, vcode))
