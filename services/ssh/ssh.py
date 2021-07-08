import re 
import subprocess

class SSH():
  def __init__(self):
    self.sshPATH = "/etc/ssh/sshd_config"

    self.port = ""
    self.server_address = ""
    self.ssh_allowed_groups = ""
    self.sftp_allowed_groups = ""
    self.init_configuration()

  
  def information(self) :
    self.port = input("what port are you going to use for sftp/ssh ? ")
    self.server_address = input("what the ip address of the server ? ")
    self.ssh_allowed_groups = input("what groups is allowed to ssh (seperate each group with,) ")
    self.sftp_allowed_groups = input("what groups is only allowed to sftp (seperate each group with,) ")
    # self.port = "2020"
    # self.server_address = "10.0.0.15"
    # self.ssh_allowed_groups = "Formateur,GRPA"
    # self.sftp_allowed_groups = "sftponly"

  def init_configuration(self) :
    self.information()
    with open("Config/ssh/sshd_config","r") as file : 
      origin = file.readlines()
    #port
    origin[20] = f"{origin[20].strip()} {self.port} \n"
    #server ip address
    origin[22] = f"{origin[22].strip()} {self.server_address} \n"
    #FIRST CHECK OF ALLOWNES
    AllowGroups = ""
    if re.search(",",self.ssh_allowed_groups) !=None  : 
        AllowGroups = self.ssh_allowed_groups.split(",")
        AllowGroups = " ".join(AllowGroups)
    else :
      AllowGroups = self.ssh_allowed_groups

    AllowGroups2 = ""
    if re.search(",",self.sftp_allowed_groups) !=None :
        AllowGroups2 = self.sftp_allowed_groups.split(",")
        AllowGroups2 = " ".join(AllowGroups2)
    else :
      AllowGroups2 = self.sftp_allowed_groups


    origin[120] = f"{origin[120].strip()} {AllowGroups} {AllowGroups2} \n"
    print(origin[120])
    #Allowed ssh groups
    origin[124] = f"{origin[124].strip()} {self.ssh_allowed_groups} \n"
    #Allowed sftp groups
    origin[127] = f"{origin[127].strip()} {self.sftp_allowed_groups} \n"

    with open(self.sshPATH,"w") as file :
      file.write("")
      file.writelines(origin) 

d = SSH()








