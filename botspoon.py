import os
import requests
import random
from datetime import datetime
import json
import uuid
import platform
import time
import sys
import traceback

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.2/10)


def tele(bot_message):
    
    bot_token = '1160430048:AAHWoxOJxQ8amBHh0b3CsRTz8NeXphWVf70'
    bot_chatID = '-483298315'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
   
 
def activation(bot_message):
    
    bot_token = '1160430048:AAHWoxOJxQ8amBHh0b3CsRTz8NeXphWVf70'
    bot_chatID = '-426516657'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)



def signa():
	
	os.system('clear')
	#print("\033[1;34;42m")
	print("\033[1;35;44m")
	print("BlitzKrieg")
	print("CP : 085155415154\n")
	print(datetime.now())
	print("VERSI : VIP")
	#print(pess)
	print("\033[1;37;40m\n")
	
def sign(pess):
	
	os.system('clear')
	#print("\033[1;34;42m")
	print("\033[1;35;44m")
	print("BlitzKrieg")
	print("CP : 085155415154\n")
	print(datetime.now())
	print("VERSI : VIP")
	print(pess)
	print("\033[1;37;40m\n")


	
if __name__ == "__main__":
	try:
		#saring
		if os.path.exists('../botspoon/000aktivasi.johnson') == True:
			namaaktivasi='../botspoon/000aktivasi.johnson'
		else:
			namaaktivasi='000aktivasi.johnson'
		
		kode=0
		print("sedang mengecek ...")
		print("sedang memuat ...")
		print("pastikan internet aman ...")
		req = requests.get('http://keple.site/spoon/fun.fun').text
		
		act = requests.get('http://keple.site/spoon/kodefun')
		
		active = act.json()['kode']
		#active = requests.get('https://diveot.site/spoon/kodecat').json()['kode']
		
		imei = act.json()['imei']
		#imei = requests.get('https://diveot.site/spoon/imei').json()['imei']
		perangkat = act.json()['perangkat']
		ver = act.json()['versi']
		os.system('clear')
		print("sedang memuat ...")
		if req != "A":
			try:
				print(req)
			except:
				print("SCRIPT DIMATIKAN")
			exit()
	
		
		#pess = requests.get('https://diveot.site/spoon/pesan.txt').text
		#pesse = requests.get('https://diveot.site/spoon/ucingmessage.json')
		#pesen = pesse.json()
		
		
		#print(pess)
		#time.sleep(10)
		
		#aktivasi = zz.json()['kode']
		
		#print(aktivasi)
		#cur_path = os.path.dirname(__file__)
		#new_path = os.path.relpath('..\\subfldr1\\testfile.txt', cur_path)
		#with open(new_path, 'w') as f:
			#f.write(data)
		signa()
		
		
		
		#proses aktivasi
		with open(namaaktivasi, "r") as jsonFile:
			aktivasi = json.load(jsonFile)
		
		
		if aktivasi['kode'] not in active:
			if aktivasi['kode']==0:
				
				while(aktivasi['nama']==""):
					print('nama tidak boleh kosong')
					aktivasi['nama']=input('Masukkan nama sesuai yang diperintahkan : ')
					if aktivasi['nama']!="":
						with open(namaaktivasi, "w") as jsonFile:
							json.dump(aktivasi, jsonFile)
				
				abc=random.randint(100000,999999)
				aktivasi['kode']=abc
				
				with open(namaaktivasi, "w") as jsonFile:
					json.dump(aktivasi, jsonFile)
				
				activation(str(datetime.now())[:19]+'\n-'+str(aktivasi['nama'])+'\n-'+str(aktivasi['kode'])+'\n-'+str(uuid.uuid1())[24:]+'\n-'+str(platform.platform())+'\n'+platform.version()[15:])
				activation('\['+str(aktivasi['kode'])+',')
				activation('\["'+str(uuid.uuid1())[24:]+'",')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				print('KODE ANDA : '+str(aktivasi['kode']))
				print('\n\nPERINGATAN !!!')
				print('BACA ATAU TIDAK BACA DIANGGAP SUDAH BACA')
				print('JANGAN SEBAR KODE INI KESIAPAPUN')
				print('KECUALI PENJUAL')
				print('MELANGGAR PERATURAN INI DAPAT MENGAKIBATKAN PEMATIAN KODE')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				
				
				exit()
				
				
				
			else:
				while(aktivasi['nama']==""):
					print('nama tidak boleh kosong')
					aktivasi['nama']=input('Masukkan nama sesuai yang diperintahkan : ')
					if aktivasi['nama']!="":
						with open(namaaktivasi, "w") as jsonFile:
							json.dump(aktivasi, jsonFile)
					
				activation(str(datetime.now())[:19]+'\n-'+str(aktivasi['nama'])+'\n-'+str(aktivasi['kode'])+'\n-'+str(uuid.uuid1())[24:]+'\n-'+str(platform.platform())+'\n'+platform.version()[15:])
				activation('\['+str(aktivasi['kode'])+',')
				activation('\["'+str(uuid.uuid1())[24:]+'",')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				print('KODE ANDA : '+str(aktivasi['kode']))
				print('\n\nPERINGATAN !!!')
				print('BACA ATAU TIDAK BACA DIANGGAP SUDAH BACA')
				print('JANGAN SEBAR KODE INI KESIAPAPUN')
				print('KECUALI PENJUAL')
				print('MELANGGAR PERATURAN INI DAPAT MENGAKIBATKAN PEMATIAN KODE')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				
				
				exit()
		
		else:
			print('KODE sudah aktif')
			time.sleep(.3)
		
		
		if str(uuid.uuid1())[24:] not in imei:
			
			if str(platform.platform()).translate({ord(i): None for i in '-+ .'}) in perangkat:
				
				if str(platform.version())[15:] in ver:
					pass
				
				else:
					print('Perangkat ini di ban oleh mimin')
					activation('Aktivitas Illegal \nFUN versi\n'+str(datetime.now())[:19]+'\n'+str(aktivasi['kode'])+'\n'+str(aktivasi['nama'])+'\n'+str(uuid.uuid1())[24:]+'\n'+platform.platform())
					activation('\["'+str(platform.version())[15:]+'",')
					exit()
					
				
				
			else:
				
				#print(str(platform.platform()).translate({ord(i): None for i in '-+ .'}))
				#print(perangkat)
				print('Perangkat ini di ban oleh mimin')
				activation('Aktivitas Illegal \nFUN platform\n'+str(datetime.now())[:19]+'\n'+str(aktivasi['kode'])+'\n'+str(aktivasi['nama'])+'\n'+str(uuid.uuid1())[24:]+'\n'+platform.platform())
				activation('\["'+str(platform.platform()).translate({ord(i): None for i in '-+ .'})+'",')
				activation('\["'+str(platform.version())[15:]+'",')
				exit()
			
			
			
		
		
		
		#pw = zz.json()['password']
		#print(pw)
		#pww = input("masukkan password: ")
		#while pww != pw:
			#print("password salah")
		#	exit()
		slowprint("SELAMAT DATANG")
		tele(str(datetime.now())[:19]+'\n-'+aktivasi['nama']+' '+str(aktivasi['kode'])+' FUN \n-'+str(uuid.uuid1())[24:]+'\n-'+str(platform.platform())+'')
		os.system('clear')
		slowprint("enjoy")
		#os.system('ssh winda@107.174.64.239')
		os.system('ssh botspoon@107.175.37.133')
	except Exception as e:
		print(e)
		print(traceback.format_exc())
		exit()


