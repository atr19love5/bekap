import pytz
from datetime import datetime



tz = pytz.timezone("Asia/Jakarta")                               #2022-10-20 05:04:10
now = datetime.now(tz)
waktu = now.strftime("%Y-%m-%d %H:%M:%S")
print(waktu)
input()