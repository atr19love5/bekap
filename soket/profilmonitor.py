from tinydb import *

from colorama import Fore, Style, init
init()


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

db = TinyDB("datamonitor.json")
q = Query()
polp=input("Reset data [y], Enter to skip")
if polp=="y":
    db.truncate()
    db.insert({"game": "monitor", "data":{
        "id": "",
        "room":"",
        "nickname":"",
        "type":"",
        "data":""
        }})
    db.insert({"game": "buntut", "data":{
        "enter": ["lah nama baru dateng"],
        "chat": ["nama yang suka keliling kan ya?"],
        "nick":"",
        "on":False
        }})
ppp="""
ataro=1119943580
kang adu domba=1070367332
"""
print(ppp)
menu="""
1. change id
2. buntutin
"""
while True:
    db = TinyDB("datamonitor.json")
    q = Query()
    dataxyz=db.search(q.game == 'monitor')[0]["data"]
    databuntut=db.search(q.game == 'buntut')[0]["data"]
    print(menu)
    pil=input("menu ke :")
    if pil=="1":
        dataxyz["id"]=input("ID : ")
        print("  id\t: "+c("yellow",dataxyz["id"],0))

        db.update({'data': dataxyz}, where('game') == "monitor")
    elif pil=="2":
        while True:
            print("""\nq for exit
1. add enter "lah nama baru dateng"
2. add chat "nama yang suka keliling kan ya?"
3. panggilan "bang jo" 
4. y/n [q exit]""")
            inp=input("> ")
            if inp=="q":
                break
            elif inp=="1":
                databuntut["enter"].append(input("enter :"))
                db.update({'data': databuntut}, where('game') == "buntut")
                print("  enter\t: "+c("yellow",databuntut["enter"],0))
            elif inp=="2":
                databuntut["chat"].append(input("chat :"))
                db.update({'data': databuntut}, where('game') == "buntut")
                print("  chat\t: "+c("yellow",databuntut["chat"],0))
            elif inp=="3":
                databuntut["nick"]=input("panggilan :")
                db.update({'data': databuntut}, where('game') == "buntut")
                print("  nick\t: "+c("yellow",databuntut["nick"],0))
            elif inp=="4":
                inp=input(" on? > ")
                if inp=="y":
                    databuntut["on"]=True
                    db.update({'data': databuntut}, where('game') == "buntut")
                    print("  mode\t: "+c("yellow",databuntut["on"],0))
                elif inp=="n":
                    databuntut["on"]=False
                    db.update({'data': databuntut}, where('game') == "buntut")
                    print("  mode\t: "+c("yellow",databuntut["on"],0))

