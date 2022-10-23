import json

import pyrebase

config=json.loads(open("dbaddrs.json","r").read())
firebase = pyrebase.initialize_app(config)
db = firebase.database()

req = db.child('account').child('uid').child('results').child(0).get().val()
print(json.dumps(req))








