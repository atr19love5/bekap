
import subprocess
import pyrebase
import json

config=json.loads(open("dbaddrs.json","r").read())


firebase = pyrebase.initialize_app(config)
db = firebase.database()


while True:
    dbb = {"results": []}
    req = db.child('yoha').child('akun').child("results").get()
    acc = req.val()
    for tott in acc:
        dbb["results"].append(tott)

    tet = 1
    for ppp in dbb["results"]:
        print(f'{tet}. {ppp["no"]}')
        tet += 1

    print(f"total uid : {len(dbb['results'])}")

    nuid = input("insert No : ")
    nupass = input("insert Pass : ")
    nuall={"no":nuid,"pass":nupass}
    dbb["results"].append(nuall)
    print(f"total uid : {len(dbb['results'])}")

    # print(json.dumps(dbb, indent=2))
    db.child("yoha").child("akun").update(dbb)
