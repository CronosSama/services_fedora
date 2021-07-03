import subprocess
class INSTALLER() :

  def __init__(self,service):
      self.service = service
      self.packages_path = []
      self.CALLER()

  def FTP(self) :
    self.packages_list= ["./packages/vsftpd-3.0.3-44.fc35.x86_64.rpm"]

  def install(self):
    for package in self.packages_list :
      subprocess.run(f"sudo dnf localinstall {package}",shell=True)

  def CALLER(self):
    if self.service == "FTP" :
      self.FTP()
      self.install()





















