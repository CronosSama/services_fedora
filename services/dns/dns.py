import re
import subprocess
class DNS():
  def __init__(self,serverIP,prefix,networkAddress,reversed_,domain_name,hostname):

     self.named_PATH = "/etc/named.conf"
     self.direct_zone_PATH = ""
     self.reverse_zone_PATH = ""
     self.allowedNetworks = [networkAddress]
     self.prefix = prefix
     self.dns_server_ip = serverIP
     self.address_riversed =  reversed_
     self.domain_name = domain_name
     self.server_hostname = hostname
     self.NStype = "master"
     #for adding entry to the zone files
     self.entryName = "web"
     self.entryIP = self.dns_server_ip
     self.entryType = "A"
     #self.init_configuration()
     self.init_configuration()
     self.ADD_ENTRY()
     self.entryIP = "web"
     self.entryName = "www"
     self.entryType = "CNAME"
     self.ADD_ENTRY()
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


  def init_information(self,init=False):
    self.domain_name = input("what is the domain name ? ")
    if init == True : 
      self.allowedNetworks.append(input("what network you want to allow ? "))
      self.prefix = input("what is the prefix of your network ?")
      self.dns_server_ip = input("what is the ip address of the dns server ? ")
      self.server_hostname = input("what the server hostname ? ")
      self.address_riversed = input("what the address reversed ? ")


      # self.allowedNetworks.append("10.0.0.0")
      # self.dns_server_ip = "10.0.0.15"
      # self.server_hostname = "srv1"
      # self.address_riversed = "0.0.10"
      #some magic will happen and will do the initial configuration 
    else : 
      self.entryName = input("what is the hostname ? ")
      self.entryIP = input("what is the address Ip or cname of the host ?  ")
      self.entryType = input("what is the entry type ? ")


  def init_configuration(self) : 
        # self.init_information(True)
        with open("Config/dns/named.conf","r") as file : 
          named = file.readlines()
        #ADD ACE
        position = self.getPosition(named,"acl","}")
        named.insert(position[0]+1,f"{self.allowedNetworks[0]}/{self.prefix} ;\n")
        #ADD SERVER IP
        position = self.getPosition(named,"listen-on port 53")
        named[position[0]] = named[position[0]].strip() + self.dns_server_ip.strip() + "; };\n"
        ###ZONEFILES
        ##DIRECT
        position = self.getPosition(named,"#DIRECT")
        #zone with domain name
        named[position[0]+1] = f'zone "{self.domain_name}" IN '+" { \n"
        #zone type
        named[position[0]+2] = named[position[0]+2].strip() + f" {self.NStype} ;\n"
        #zone file name
        named[position[0]+3] = named[position[0]+3].strip() + f' "{self.domain_name}" ;\n'
        self.cmd(f"touch /var/named/{self.domain_name}")

        ##REVERSE
        position = self.getPosition(named,"#REVERSE")
        #zone with reversed
        named[position[0]+1] = f'zone "{self.address_riversed}.in-addr.arpa" IN '+"{ \n"
        #ZONE type
        named[position[0]+2] = named[position[0]+2].strip() + f" {self.NStype} ;\n"
        reversed_domain = self.domain_name.split(".")
        reversed_domain = ".".join(reversed_domain[::-1])
        #ZONE FILE
        named[position[0]+3] = named[position[0]+3].strip() + f' "{reversed_domain}" ;\n'
        self.cmd(f"touch /var/named/{reversed_domain}")
        with open(self.named_PATH,"w") as file :
          file.write("") 
          file.writelines(named)

        with open("Config/dns/header.lab","r") as file :
          header_direct = file.readlines()
          file.seek(0)
          header_inverse =  file.readlines()
        
        position = self.getPosition(header_direct,"SOA")
        header_direct[position[0]] = f"{header_direct[position[0]].strip()} {self.server_hostname}.{self.domain_name}. root.{self.domain_name}. ( \n" 
        header_inverse[position[0]] = f"{header_inverse[position[0]].strip()} {self.server_hostname}.{self.domain_name}. root.{self.domain_name}. ( \n" 

        position = self.getPosition(header_direct,"NS")
        header_direct[position[0]] = f"{header_direct[position[0]].strip()} \t {self.server_hostname}.{self.domain_name}. \n"
        header_inverse[position[0]] = f"{header_inverse[position[0]].strip()} \t {self.server_hostname}.{self.domain_name}. \n"

        position = self.getPosition(header_direct,"IN  A")
        header_direct[position[0]] = f"{header_direct[position[0]].strip()} \t {self.dns_server_ip} \n"
        header_direct.insert(position[0]+1,f"{self.server_hostname}\tIN\tA\t{self.dns_server_ip} \n")
        last_octet = self.dns_server_ip.split(".")
        # header_inverse.insert(position[0],f"{last_octet[-1]}\tIN\tPTR\t{self.server_hostname}.{self.domain_name} \n")
        header_inverse[position[0]] = f"{last_octet[-1]}\tIN\tPTR\t\t{self.server_hostname}.{self.domain_name} \n"

        self.direct_zone_PATH = f"/var/named/{self.domain_name}"
        self.reverse_zone_PATH = f"/var/named/{reversed_domain}"

        
        with open(self.direct_zone_PATH,"w") as file :
          file.write("")
          file.writelines(header_direct)
        
        with open(self.reverse_zone_PATH,"w") as file :
          file.write("")
          file.writelines(header_inverse) 

        with open("Config/dns/path","w") as file : 
          file.write(f"{self.direct_zone_PATH} \n")
          file.write(f"{self.reverse_zone_PATH}")

        self.cmd(f"chown named:named {self.direct_zone_PATH}")
        self.cmd(f"chown named:named {self.reverse_zone_PATH}")




  def ADD_ENTRY(self) : 
    # self.init_information()
    self.get_path()
    with open(self.direct_zone_PATH,"r") as file :
      direct = file.readlines()
    
    with open(self.reverse_zone_PATH,"r") as file :
      inverse = file.readlines()

    direct.insert(len(direct),f"{self.entryName}\tIN\t{self.entryType}\t{self.entryIP}\n")
    if self.entryType != "CNAME" : 
      self.entryIP = self.entryIP.split(".")
      inverse.insert(len(inverse),f"{self.entryIP[-1]}\tIN\tPTR\t{self.entryName}.{self.domain_name}\n")
    else : 
      pass

    with open(self.direct_zone_PATH,"w") as file :
      file.write("")
      file.writelines(direct)
    
    with open(self.reverse_zone_PATH,"w") as file :
      file.write("")
      file.writelines(inverse) 

  def DELETE_ENTRY(self) : 
    self.entryName = input("what the entry name ? ")
    self.get_path()
    with open(self.direct_zone_PATH,"r") as file :
      direct = file.readlines()
    
    with open(self.reverse_zone_PATH,"r") as file :
      inverse = file.readlines()

    direct_position = self.getPosition(direct,self.entryName)

    if  re.search("CNAME",direct[direct_position[0]]) == None  :

      position = self.getPosition(inverse,self.entryName) 
      inverse[position[0]] = ""
    else : 
      pass

    direct[direct_position[0]] = ""
    with open(self.direct_zone_PATH,"w") as file :
      file.write("")
      file.writelines(direct)
    
    with open(self.reverse_zone_PATH,"w") as file :
      file.write("")
      file.writelines(inverse) 

  def get_path(self) : 
    with open("Config/dns/path","r") as file :
      paths = file.readlines()
    self.direct_zone_PATH = paths[0].strip()
    self.reverse_zone_PATH = paths[1].strip()
 
  def cmd(self,command):
    subprocess.run(command,shell=True)






