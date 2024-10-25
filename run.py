
#---------color code--------#
I='\033[1;32m'
Q="\x1b[00m"
dt = f"{Q}[{I}•{Q}]"
n = '\n'
#---------import------------#
import os, sys
import time
import requests 
from requests.structures import CaseInsensitiveDict
import random

os.system("clear")
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White
print(bired+"""
\033[1;97m

██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
        

\033[1;96m__________________________________________________
__________________________________________________

\033[1;92m[•] WELC0ME DH TOOLS USER
\033[1;91m[•] CUSTOM SMS SENDER TOOLS 
\033[1;92m[•] PLEASE USERNAME AND PASSWORD                        
\033[1;96m__________________________________________________
__________________________________________________

""")




def DH():
  import sys
while True:
    usern="DH Alamin Hasan"
    passwd="Dark-Hunter"
    inpuser=str(input(bigreen+" \033[1;97m[•] Enter Your Username: "))
    
    inppass=str(input(" \033[1;97m[•] Enter Your Password: "))
    
    if usern==inpuser and passwd==inppass:
    	print(bigreen+" [√]User & Password Correct !")
    	break
    else:
    	print(bired+" [×] Wrong User or Password !")
    	Please_Try_Again()
    	os.system('xdg-open https://github.com/DH-Alamin')
os.system("clear")






#--------logo-------------#
logo=('''\033[1;97m

██████╗░██╗░░██╗
██╔══██╗██║░░██║
██║░░██║███████║
██║░░██║██╔══██║
██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝   


██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

\033[1;97mTOOLS OWNER : \033[1;97mDH ALAMIN HASAN \033[1;97m[Dark-Hunter]
\033[1;97mT00LS       : \033[1;97mCUSTOM SMS/CUSTOM SMS BOMBING
\033[1;97mGITHUB      : \033[1;97mGithub.com/DH-Alamin
\033[1;97mVERSION     : \033[1;91m2.0.0 {🔥}

\033[1;97m__________________________________________________
\033[1;97m__________________________________________________
''')
#..............clear.......#
def clear():
  os.system("clear")
#---------menu-----------#
def menu():
  clear()
  print(logo)
  print(f' {dt} [01] CUSTOM SMS')
  print(f' {dt} [02] CUSTOM SMS BOMBER')
  print(f' {dt} [03] TOOLS OWNER')
  print(f' {dt} [04] EXIT')
  user = input(f' {dt} CHOICE OPTION : ')
  if user in ['01', '1']:
    custom()
    
  elif user in ['02', '2']:
    customb()
  elif user in ['03', '3']:
    os.system('xdg-open https://www.facebook.com/DH.Alamin.Hasan01')
  else:
    exit(f' {dt} THANKS FOR USEING MY TOOLS ')
    
#-----------custom sms-----------#
def custom():
  clear()
  print(logo)
  nmbr=input(f' {dt} ENTER NUMBER : ')
  msg=input(f' {dt} ENTER MESSAGE : ')
  
  api = f'https://api.smsinbd.com/sms-api/sendsms?api_token=0bCYbXgzq19vnbuVYIy0btHk4KAKkalhVnh52fB2&senderid=8801969908462&message={msg}&contact_number={nmbr}'
  requests.get(api)
  print(f'SMS Send Successful')
  time.sleep(5.09)
  os.system('xdg-open https://www.facebook.com/DH.Alamin.Hasan01')
  menu()
  
#----------custom sms bomber---------#
def customb():
  clear()
  print(logo)
  nmbr=input(f' {dt} ENTER NUMBER : ')
  msg=input(f' {dt} ENTER MESSAGE : ')
  
  lmt = int(input(f' {dt} ENTER AMOUNT : '))
  for i in range(lmt):
    api = f'https://api.smsinbd.com/sms-api/sendsms?api_token=0bCYbXgzq19vnbuVYIy0btHk4KAKkalhVnh52fB2&senderid=8801969908462&message={msg}&contact_number={nmbr}'
    requests.get(api)
    print((str(i+1))+f' {dt} SMS Send Successful  \n')
  print('Custom SmS Bombing Successful')
  time.sleep(5.09)
  os.system('xdg-open https://www.facebook.com/DH.Alamin.Hasan01')
  menu()
#-----------end-------------#
menu()
