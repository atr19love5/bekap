import pyrebase,json


config=json.loads(open("dbaddrs.json","r").read())


firebase = pyrebase.initialize_app(config)
db = firebase.database()


def token():
    tkn = db.child('yoha').child('token').get()
    acc = tkn.val()["results"]
    return acc


def uid():
    tkn = db.child('yoha').child('akun').get()
    acc = tkn.val()["results"]
    return acc
