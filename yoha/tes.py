import pyrebase,json,getapi

config=json.loads(open("dbaddrs.json","r").read())


firebase = pyrebase.initialize_app(config)
db = firebase.database()

tkn = db.child('yoha').child('token').child("results").child(4).get().val()

print(tkn)
xxp=getapi.claim(tkn)

print(xxp)