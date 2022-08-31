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
api_id = "#ايبي ايديحطه هنا"
api_hash = "ايبي هاش حطه هنا "
ID = "ايديك"
token= "توكنك"
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
            print(F+'Approved✅ | Dev : whitepro.')
            mgs=f'''• 𝖭𝖾𝗐 𝖵𝗂𝗌𝖺 𝖼𝗁𝖾𝖼𝗄𝖾𝖽 𝖻𝗒 𝖼𝗈𝗆𝖻𝗈✅.
{ccn} .
𝖣𝖾𝗏♕ : @z_w_t
𝖡𝗒🀠: 𝖶𝗁𝗂𝗍𝖾 𝗉𝗋𝗈'''
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else :
            print(Z+'Declined❌ | Dev : whitepro.')
    except:
        print(False)
        #whitepro