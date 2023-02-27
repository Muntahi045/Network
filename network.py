import socket
import sys,os
os.system("clear")
print(""" \033[0;35m
__  __             _        _     _
|  \/  |_   _ _ __ | |_ __ _| |__ (_)
| |\/| | | | | '_ \| __/ _` | '_ \| |
| |  | | |_| | | | | || (_| | | | | |
|_|  |_|\__,_|_| |_|\__\__,_|_| |_|_|

""")

print ("\033[4;34mEnter your target")
hostname = input (":\033[4;32m ")
ip=socket.gethostbyname(hostname)

print ('\033[0;33mhostname is >>',hostname, '\n' 'target is >>',ip)

print("\033[0;35my/n")
o = input ("\033[0;36mwant you start agen?: ")

if o == 'y' :
	os.system("python network.py")
	
elif o == 'n' :
	print("\033[0;32thank you for use this tool")