from services.dhcp.dhcp import DHCP
import subprocess



class CONFIGURER() :
  def __init__(self,service,option=""):
      self.option = option
      self.service = service
      self.initial_State = "no"
      self.config_list = []
      self.PATH = ""
      self.configuration = {}
      self.CALLER()

  def doer(self):
    with open(self.PATH,"r") as config_file :

      self.config_list=config_file.readlines()
      for ligne_number,value in self.configuration.items() :
        self.config_list[ligne_number]=f"{value}\n"

    with open(self.PATH,"w") as config_file :
      config_file.writelines(self.config_list)
    
    self.reset()
    
  def FTP(self) :
    #self.PATH = "./Config/vsftpd.conf"
    self.PATH = "/etc/vsftpd/vsftpd.conf"
    self.configuration = {11:"anonymous_enable=NO",113:"listen=YES",122:"listen_ipv6=NO"}
    self.RESTARTER()

  def DHCPD(self) :
    DHCP(self.option)
    print("RESTART will start now ...")
    self.RESTARTER()  
 
    


  def CALLER(self) :
    if self.service == "vsftpd" :
      self.FTP()
      self.doer()
    if self.service == "dhcpd" :
      self.DHCPD()

  def cmd(self,command) :
    subprocess.run(command,shell=True)

  def reset(self) :
    self.PATH = ""
    self.configuration = {}
    self.config_list = []


  def RESTARTER(self) :
    self.cmd(f"service {self.service} restart")