#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import optparse
import re
import sys

class MacChanger():
	def __init__(self):
		self.description=""
		self.kullanim=""
		if sys.version_info[0] >= 3:
			self.desciption = "Mac Adresi Değiştirme Python Scripti"
			self.kullanim = "Örnek Kullanım: python macChanger.py --arayuz wlan0 --mac 00:11:99:88:77:66"
		else:
			self.desciption = unicode("Mac Adresi Değiştirme Python Scripti", "utf8")
			self.kullanim = unicode("Örnek Kullanım: python macChanger.py --arayuz wlan0 --mac 00:11:99:88:77:66", "utf8")

	def arguman_al(self):
		parse=optparse.OptionParser(description=self.desciption,prog='macChanger',epilog=self.kullanim)
		parse.add_option("-i","--arayuz",dest="arayuz",help="Mac adresinin degistirilecegi arayuz")
		parse.add_option("-m","--mac",dest="mac",help="Yeni MAC adresi")
		(options,arguments)= parse.parse_args()
		if not options.arayuz:
			parse.error("[-] Lütfen bir arayüz belirtin,daha fazla bilgi için --help kullanın.")
		elif not options.mac:
			parse.error("[-] Lütfen yeni bir mac adresi giriniz,daha fazla bilgi için --help kullanın.")
		else:
			return options


	def mac_degistir(self,arayuz,mac):
		print("[+] "+arayuz+" arayüzü için mac adresi "+mac+	" olarak değiştiriliyor.")
		subprocess.call(["ifconfig",arayuz,"down"])
		subprocess.call(["ifconfig",arayuz,"hw","ether",mac])
		subprocess.call(["ifconfig",arayuz,"up"])


	def mac_getir(self,arayuz):
		ifconfig_sonuc=subprocess.check_output(["ifconfig",arayuz])
		ifconfig_sonuc=str(ifconfig_sonuc)
		mac_adres_arama_sonuc=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_sonuc)

		if mac_adres_arama_sonuc:
			return mac_adres_arama_sonuc.group(0)
		else:
			print("[-] Mac adresi okunamadı!")

	def mac_adresi_durum(self):
		if self.mac_getir(options.arayuz) == options.mac:
			print("[+] Mac adresi başarıyla " + self.mac_getir(options.arayuz) + " olarak değiştirildi.")
		else:
			print("[-] Mac adresi değiştirilemedi!")

	def suanki_mac(self,arayuz):
		mac=self.mac_getir(str(arayuz))
		print("Şuanda kullanılan  Mac adresi:"+str(mac))


macChanger=MacChanger()
options=macChanger.arguman_al()
macChanger.suanki_mac(options.arayuz)
macChanger.mac_degistir(options.arayuz,options.mac)
macChanger.mac_adresi_durum()


