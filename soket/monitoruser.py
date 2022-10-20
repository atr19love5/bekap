import time,os
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
print("\nbuka profilemonitor sama openallroom dulu bro")

while True:
    db = TinyDB("datamonitor.json")
    q = Query()
    try:
        os.system("cls")
        print()
        result = db.search(q.game == 'monitor')[0]["data"]
        print("  id\t: "+c("yellow",result["id"],0))
        print("  nick\t: "+c("cyan",result["nickname"],0))

        print("  type\t: "+c("yellow",result["type"],0))
        print("  room\t: "+c("yellow",result["room"],0))
        print("  data\t: "+c("green",result["data"],0))

        
        result = db.search(q.game == 'buntut')[0]["data"]
        print("\n  enter\t: "+c("cyan",result["enter"],0))
        print("\n  chat\t: "+c("yellow",result["chat"],0))
        print("  nick\t: "+c("cyan",result["nick"],0))
        if result["on"]:
            print("  on\t: "+c("green",result["on"],0))
        else:
            print("  on\t: "+c("red",result["on"],0))
    except Exception as e:
        print(f"  Error : {e} ")
    time.sleep(1)
