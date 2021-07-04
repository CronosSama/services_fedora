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
    
  def DHCP(self) :
    # self.PATH = "/etc/dhcp/dhcpd.conf"

    if self.option == "ADD_NETWORK" :
      inputs = ["subnet","netmask","range","dns-server","domain-name","default-gateway","broadcast-address","default-lease-time","max-lease-time"]
      conf = []
      for inp in inputs :
        new = input(f"the value of {inp} : ")
        conf.append(new)
      origin = []
      with open("./Config/dhcp/add.txt","r") as file :
        origin = file.readlines()
      for i,data in enumerate(conf) :
        if i == 0 :
          origin[i] = "subnet "+conf[i]+" netmask "+conf[i+1]+" {\n"
        if i == 1 :
          pass

        else : 
          i = i-1
          origin[i]=origin[i].strip()
          origin[i] = origin[i]+" "+data+" ;\n"

        
      origin.pop()
      origin.append("} \n")
      with open("./Config/dhcp/try.txt","w") as file :
        file.writelines(origin)
    #self.cmd("cp /usr/share/doc/dhcp-server/dhcpd.conf.example /etc/dhcp/dhcpd.conf")
    


  def CALLER(self) :
    if self.service == "vsftpd" :
      self.FTP()
      self.doer()
    if self.service == "dhcpd" :
      self.DHCP()
    #self.RESTARTER()

  def cmd(self,command) :
    subprocess.run(command,shell=True)

  def reset(self) :
    self.PATH = ""
    self.configuration = {}
    self.config_list = []


  def RESTARTER(self) :
    self.cmd(f"service {self.service} restart")