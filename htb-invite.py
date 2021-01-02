# importing modules
from os import system
import base64
from termcolor import colored

# colors
cn = 'cyan'

# installing requirements
req = input(colored("Do you want to install the requirements ( y / n) ",cn))

if req == "y":
	print(colored("\nYou must be a root user to install requirements!\n",cn))
	print(colored("\nIf it asks for password please Enter it!\n",cn))
	system('sudo apt install figlet')
	system('git clone https://github.com/busyloop/lolcat')
	system('cd lolcat/bin && sudo gem install lolcat')

# requirements satisfied ^^

# HACKING NASA lol
system('clear')
system('figlet -f ./Bloody "HACKING NASA" | lolcat -a -d 2')
system('echo "With HTML" | lolcat -a -d 3')
print()
system('echo "You\'ve caught by NASA for HACKING lol" | lolcat -a -d 30')
print()
system('echo "Clearing your Records...." | lolcat -a -d 50')
system('clear')
system('figlet -f ./Bloody "HACKED" | lolcat -a -d 5')
print()
system('echo "Here is a sweet root shell for you ENJOY" | lolcat -a -d 40')
print()
system('echo "root@NASA~:# ls" | lolcat -a -d 5')
print()
system('echo "vanakam_nanba.sh" | lolcat -a -d 2')
print()
system('echo "root@NASA~:# _" | lolcat -a -d 45')
system('echo "^C" | lolcat -a -d 2')
system('echo "shell exited coz user have no brain lol" | lolcat -a -d 25')
# printing banner
print("\n\n")
system('figlet -f ./Bloody "H T B" | lolcat -a -d 2')
print()
system('echo "Invite code Generator By Jopraveen" | lolcat -a -d 2')
print()

# Hacking invite code
system('bash gen.sh')
