#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import optparse
import re

def arguman_al():
	parse=optparse.OptionParser()
	parse.add_option("-i","--arayuz",dest="arayuz",help="Mac adresinin degistirilecegi arayuz")
	parse.add_option("-m","--mac",dest="mac",help="Yeni MAC adresi")
	(options,arguments)= parse.parse_args()	
	if not options.arayuz:
		parse.error("[-] Lütfen bir arayüz belirtin,daha fazla bilgi için --help kullanın.")
	elif not options.mac:
		parse.error("[-] Lütfen yeni bir mac adresi giriniz,daha fazla bilgi için --help kullanın.")
	else:
		return options


def mac_degistir(arayuz,mac):
	print("[+]  "+arayuz+" arayüzü için mac adresi "+mac+	" olarak değiştiriliyor.")
	subprocess.call(["ifconfig",arayuz,"down"])
	subprocess.call(["ifconfig",arayuz,"hw","ether",mac])
	subprocess.call(["ifconfig",arayuz,"up"])


def mac_getir(arayuz):
	ifconfig_sonuc=subprocess.check_output(["ifconfig",arayuz])
	mac_adres_arama_sonuc=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_sonuc)

	if mac_adres_arama_sonuc:
		return mac_adres_arama_sonuc.group(0)
	else:
		print("[-] Mac adresi okunamadı!")	



options=arguman_al()
guncel_mac=mac_getir(options.arayuz)
print("Şuanda kullanılan  Mac adresi:"+str(guncel_mac))

mac_degistir(options.arayuz,options.mac)


guncel_mac=mac_getir(options.arayuz)
if guncel_mac==options.mac:
	print("[+] Mac adresi başarıyla "+guncel_mac+" olarak değiştirildi.")
else:
	print("[-] Mac adresi değiştirilemedi!")


