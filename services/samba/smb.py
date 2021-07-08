import re
import subprocess

class SMB():
  def __init__(self):
      self.smbPATH = "/etc/samba/smb.conf"
      # self.smbPATH = "Config/samba/smb.conf"

      self.folderName = ""
      self.theAdmin = ""
      self.validUsers = []
      self.directoryMask = ""
      self.createMask = ""
      self.writable = ""
      self.path = ""
      self.allowedHost = ""
      self.prefix = 24
      self.init_configuration()
      self.ADD_ENTRY()
      self.init_interface()
      self.cmd("service smb restart")

  def infromation(self,init=False) : 
    if init == False :
      #mnin nbghiw add chi haja jdida
      self.folderName = input("what is the folder name ? ")
      self.theAdmin = input("what the admin login name ? ")
      self.validUsers= input(f"valid user/@group (you can write more than one) :  ")
      self.serverIP = input("what is the ip address of the serevr ? ")
      self.directoryMask = input("what is the directory mask ? ")
      self.createMask = input("what is the files mask ? ")
      self.writable = input("is it writable  ? ")

      # self.folderName = "FOOOLDER"
      # self.theAdmin = "HERO"
      # self.validUsers = "@GROUPA @GROUB ANA"
      # self.directoryMask = "0777"
      # self.createMask = "0666"
      # self.writable = "yes"

      self.path = f"/share/{self.folderName}"
      self.cmd(f"mkdir /share/{self.folderName} ;chown -R {self.theAdmin}:{self.theAdmin} /share/{self.folderName}")

    else : 
      self.allowedHost = input("what is the network address ?")
      self.prefix = int(input("what is the network prefix ? [no slash] "))
      # self.allowedHost = "10.0.0.0"
      # self.prefix = 24
      self.allowedHost = self.allowedHost.split(".")
      self.allowedHost = self.allowedHost[0:int(self.prefix/8)]


  def init_configuration(self) : 
    self.infromation(True)
    lol = []
    with open("Config/samba/origin.conf","r") as file :
      lol = file.readlines()
    position = self.getPosition(lol,"hosts allow = ")
    joined = ".".join(self.allowedHost)
    lol[position[0]] = f"\t{lol[position[0]].strip()} {joined}. \n "

    with open(self.smbPATH,"w") as file : 
      file.write("")
      file.writelines(lol)

  def ADD_ENTRY(self) : 
    self.infromation()
    
    with open(self.smbPATH,"r") as file :
      origin = file.readlines()
    origin.append(f"[{self.folderName}] \n")
    origin.append(f"\tpath = {self.path} \n")
    origin.append(f"\tvalid users = {self.validUsers} {self.theAdmin} \n")
    origin.append(f"\twritable = {self.writable} \n")
    origin.append(f"\tdirectory mask = 0{self.directoryMask} \n")
    origin.append(f"\tcreate mask = 0{self.createMask} \n")

    with open(self.smbPATH,"w") as file :
      file.write("")
      file.writelines(origin)   



  def init_interface(self):
    interface = subprocess.run("ifconfig | head -1 | cut -d: -f1",shell=True,capture_output=True)
    interface = interface.stdout.decode().strip()
    # print(interface.stdout.decode().strip())
    self.cmd(f"nmcli connection modify {interface} IPv4.address {self.serverIP}/{self.prefix} ")
    self.cmd(f"nmcli connection modify {interface} IPv4.dns {self.serverIP} ")
    self.cmd(f"nmcli connection modify {interface} IPv4.method manual ")
    arrayed_ip = self.serverIP.split(".")
    arrayed_ip[-1] = "1"
    arrayed_ip = ".".join(arrayed_ip)
    self.cmd(f"nmcli connection modify {interface} IPv4.gateway {arrayed_ip}")
    self.cmd(f"nmcli connection down {interface} ")
    self.cmd(f"nmcli connection up {interface} ")



  def cmd(self,command):
    subprocess.run(command,shell=True)



  def getPosition(self,file,first,end=False) :
    #daba plan wmafih anaho ana tan9lb 3la wa7d l3iba tatbda bchi l3iba "first"
    # had l3iba tatkml bchi l3iba okhra tanprovidiha f "end", w brit index fin taykml 7ta howa 
    # tandiro return wa7d array fih index dyal lbdya wdyal nihaya
    array = []
    for index,item in enumerate(file) :
      search = re.search(first,item)
      if search != None : 
        array.append(index)
        #hadi drtha bach mnin yl9a hadak first wtan7to index dyalo
        #nnbdlo valeur dyal first b valeur dyal end bach y9lb 3liha
        #blast mandiro wa7d for loop okhra wla variable okhra
        first = end
        #hadi mnin yl9a dakchi li khasni fi 7alat 3tito first w end safi critiria lwla hatkhdm w ytra loop break
        #tanya hiya fi7alat tansearchi her 3la index dyal chi kalma wla jomla safi wmam7tajch end
      if len(array) == 2 or (len(array) == 1 and end == False) :
        break
    return array




x = SMB()




