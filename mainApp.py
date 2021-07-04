from installer import INSTALLER
from configurer import CONFIGURER
import time
import subprocess

# variable = subprocess.run("tr a-z A-Z < ./hero  1>> ./shero",capture_output=True,shell=True)
# print(variable.stdout.decode())

class BASED_APP() :
  def __init__(self):
      self.mainMSG = "[0]INSTALL\t[1]CONFIGURE\t[2]CREATE_USERS\n[3]CHECK_STATUS\t[4]RESET\t[5]EXIT \n"
      self.installMSG = "[0]DHCP\t[1]DNS\t[2]HTTP\t[3]SSH\n[4]SFTP\t[5]SAMBA\t[6]EXIT\n"
      self.DHCP = "[0]ADD_NETWORK\t[1]ADD_FIXED\t[2]MODIFY_NETWORK\n[3]MODIFY_FIXED\t[4]DELETE_NETWORK\t[5]DELETE_FIXED\n[6]EXIT\n"
      self.mainSTATE = False
      self.board()

  def board(self):
    while self.mainSTATE != True :
      TOF = int(input(self.mainMSG))
      if TOF == 0 :
        self.clear()
        self.install()

      if TOF == 1 :
        self.clear()
        self.configure()

      if TOF == 5 :
        self.clear()
        print("bye bye")
        break




  def install(self):
    while self.mainSTATE != True :
      TOF = int(input(self.installMSG))
      if TOF == 4 :
        INSTALLER("vsftpd")
        break
      if TOF == 6 :
        self.clear()
        break


  def configure(self) :
    while self.mainSTATE != True :
      TOF = int(input(self.installMSG))
      if TOF == 4 :
        CONFIGURER("vsftpd")
        print("done")
        break
      if TOF == 0 :
        while self.mainSTATE !=True :
          TOF = int(input(self.DHCP))
          if TOF == 0 :
            CONFIGURER("dhcpd","ADD_NETWORK")
          if TOF == 6 :
            self.clear()
            break
        pass
      if TOF == 6 :
        self.clear()
        break  




  def clear(self):
    subprocess.run("clear")




x = BASED_APP()

