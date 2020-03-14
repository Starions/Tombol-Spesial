import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')                                                                                                                           
print "\033[91m=========================================="
print "= AUTHOR     :  Mr.St4ri0nS        "
print "= FACEBOOK   :  Wong Urep         "
print "= Github     :  github.com/TomCat394"
print "=========================================="
print "\033[97m     [+] STARIVER Cyber Network [+]"
sleep(3)
print('\n\033[95mMenambahkan Tombol Spesial...')
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[+] Tunggu Sebentar...  !')
os.system('termux-reload-settings')
sleep(6)
print(a+'[+] Tombol Spesial Berhasil Di Tambahkan !! ^^'+c+'\n\n\n\n')
print "\033[94mSilahkan Mulai Ulang Aplikasi Termux Anda"
