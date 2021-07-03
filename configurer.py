



class CONFIGURER() :
  def __init__(self,service):
      self.service = service
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

  def CALLER(self) :
    if self.service == "FTP" :
      self.FTP()
      self.doer()


  def reset(self) :
    self.PATH = ""
    self.configuration = {}
    self.config_list = []