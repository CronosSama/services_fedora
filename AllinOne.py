from services.mail.mail import Mail
from configurer import CONFIGURER
from services.ssh.ssh import SSH
from services.samba.smb import SMB
from services.dns.dns import DNS
from services.dhcp.dhcp import DHCP
import subprocess

class ALL():
  def __init__(self):
    self.serverIP = ""
    self.prefix = 24
    self.gateway = ""
    self.hostname = ""
    self.NETID_OCTET = ""
    self.networkAddress = ""
    self.mask = []
    self.broadcast = ""
    self.domain_name = ""
    self.reversed = ""
    self.admin = ""
    self.interfaceName = ""
    # self.services = ["vsftpd","dhcpd","named","smb","sshd","httpd"]
    # self.firservices = ["http","ftp","http","dhcp","samba"]
    self.installs = ["dovecot","postfix"]
    self.services = ["postfix","dovecot"]
    self.firservices = ["smtp","{pop3,imap}"]
    self.install()
    # print("GATHEEERING INFORMATION TIME : \n")
    self.information()
    Mail(self.domain_name,self.hostname,self.networkAddress,self.prefix)
    # print("CONFIGURENNING INTERFACE TIME : \n")
    # self.interface()
    # print("DHCCCCCCCCCCCCCCCCCP TIME : \n")
    # self.dhcpd()
    # self.dns()
    # print("SMMMMMMMMMMMMMMMMMMMMMMMMMMMMMB \n")
    # self.smb()
    # print("SSSSSSSSSSSSSSSSSHHHHHHHHHHHD \n")
    # self.sshd()
    # print("FTTTTTTTPPPPPPPPP \n")
    # self.ftp()
    # print("SELINUX RIP TIME ::::: \n")
    # self.selinux()

    print("FINIIISH TOOOOOTCH TIME ::: \n")
    self.finish()

  def interface(self):
    interface = subprocess.run("ifconfig | head -1 | cut -d: -f1",shell=True,capture_output=True)
    interface = interface.stdout.decode().strip()
    self.cmd(f"nmcli connection modify {self.interfaceName} IPv4.address {self.serverIP}/{self.prefix} ")
    self.cmd(f"nmcli connection modify {self.interfaceName} IPv4.dns {self.serverIP} ")
    self.cmd(f"nmcli connection modify {self.interfaceName} IPv4.method manual ")
    self.cmd(f"nmcli connection modify {self.interfaceName} IPv4.gateway {self.gateway}")
    self.cmd(f"nmcli connection down {self.interfaceName} ")
    self.cmd(f"nmcli connection up {self.interfaceName} ")

  def information(self):
    self.serverIP = input("server ip :  ")
    self.prefix = int(input("prefix length : "))
    self.domain_name = input("domain-name : ")
    self.hostname = input("server hostname : ")
    #self.admin = input("admin name : ")
    #self.interfaceName = input("Interface name :")
    #self.group = input("the Name of groups (seperate each group with,) : ")
    arrayed_ip = self.serverIP.split(".")
    self.NETID_OCTET = arrayed_ip[0:3]
    for _ in self.NETID_OCTET :
      self.mask.append("255")
    self.reversed = self.NETID_OCTET[::-1]
    self.reversed = ".".join(self.reversed)
    self.mask = f'{".".join(self.mask)}.0'
    self.broadcast = f'{".".join(self.NETID_OCTET)}.255 '
    self.networkAddress = f'{".".join(self.NETID_OCTET)}.0'
    arrayed_ip[-1] = "1"

    arrayed_ip = ".".join(arrayed_ip)
    self.gateway = arrayed_ip
    print(self.serverIP,self.prefix,self.gateway,self.hostname,self.NETID_OCTET,self.networkAddress,self.mask,self.broadcast,self.domain_name,self.reversed)

  def dhcpd(self):
    DHCP("ADD_NETWORK",self.serverIP,self.prefix,self.networkAddress,self.NETID_OCTET,self.domain_name,self.gateway,self.broadcast,self.mask)

  def dns(self):
    DNS(self.serverIP,self.prefix,self.networkAddress,self.reversed,self.domain_name,self.hostname)

  def smb(self):
    groupArray = self.group.split(",")
    NETID = ".".join(self.NETID_OCTET)
    SMB(self.admin,NETID,self.prefix,groupArray)

  def sshd(self):
    SSH(self.serverIP,self.admin,self.group)

  def ftp(self):
    CONFIGURER("vsftpd")


  def finish(self):

    # self.services = ["vsftpd","dhcpd","named","smb","sshd","httpd"]

    for service in self.services :
      self.cmd(f"systemctl enable --now {service}")
    
    # self.firservices = ["http","ftp","http","dhcp","samba"]
    for firew in self.firservices : 
      self.cmd(f"firewall-cmd --add-service={firew} --permanent")

    # self.cmd("firewall-cmd --add-port=2017/tcp --permanent ")
    self.cmd("firewall-cmd --reload")


  def install(self):
    # self.installs = ["bind bind-utils","httpd","dhcp-server","samba","vsftpd"]
    for install in self.installs : 
      self.cmd(f"dnf -y install {install} ")


  def selinux(self):
    with open("/etc/selinux/config","r") as file : 
      dfile = file.readlines()

    dfile[21]="SELINUX=disabled"
    with open("/etc/selinux/config","w") as file : 
      file.write("")
      file.writelines(dfile)

  def cmd(self,command):
    subprocess.run(command,shell=True)

x = ALL()