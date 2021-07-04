import subprocess
class INSTALLER() :

  def __init__(self,service):
      self.service = service
      self.nservice = ""
      self.packages_path = []
      self.CALLER()

  def FTP(self) :
    self.packages_list= ["./packages/vsftpd-3.0.3-44.fc35.x86_64.rpm"]
    self.nservice = "ftp"

  def DHCP(self):
    self.packages_list= ["./packages/dhcp-compat-4.4.2-11.b1.fc34.x86_64.rpm"]
    self.nservice = "dhcp"

  def install(self):
    for package in self.packages_list :
      self.cmd(f"dnf localinstall {package}")

  def CALLER(self):
    if self.service == "vsftpd" :
      self.FTP()
      self.install()
    if self.service == "dhcpd" :
      self.DHCP()
      self.install()
    self.FIREWALL()
    self.STARTER()

  def cmd(self,command) :
    subprocess.run(command,shell=True)

  def STARTER(self):
    self.cmd(f"service {self.service} start")

  def FIREWALL(self):
    self.cmd(f"systemctl enable --now {self.service}")
    self.cmd(f"firewall-cmd --add-service={self.nservice} --permanent ")

















