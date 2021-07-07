import re
import subprocess
class DNS():
  def __init__(self):
     self.named_PATH = "Config/dns/named.conf"
     self.direct_zone_PATH = "Config/dns/sen.netmobo.lab"
     self.reverse_zone_PATH = "Config/dns/lab.netmobo.sen" 
     self.allowedNetworks = []
     self.dns_server_ip = ""
     self.address_riversed =  ""
     self.domain_name = ""
     self.server_hostname = ""
     self.NStype = "master"
     #for adding entry to the zone files
     self.entryName = ""
     self.entryIP = ""
     self.entryType = "A"
     #self.init_configuration()
     self.DELETE_ENTRY()
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
      self.dns_server_ip = input("what is the ip address of the dns server ? ")
      #self.domain_name = input("what is the domain name ? ")
      self.server_hostname = input("what the server hostname ? ")
      self.address_riversed = input("what the address reversed ? ")
      # self.allowedNetworks.append("10.0.0.0")
      # self.dns_server_ip = "10.0.0.15"
      # self.domain_name = "sen.netmobo.lab"
      # self.server_hostname = "srv1"
      # self.address_riversed = "0.0.10"
      #some magic will happen and will do the initial configuration 
    else : 
      self.entryName = input("what is the hostname ? ")
      self.entryIP = input("what is the address Ip or cname of the host ?  ")
      self.entryType = input("what is the entry type ? ")


  def init_configuration(self) : 
        self.init_information(True)
        with open(self.named_PATH,"r") as file : 
          named = file.readlines()
          position = self.getPosition(named,"acl","}")
          named.insert(position[0]+1,f"{self.allowedNetworks[0]} ;\n")
          position = self.getPosition(named,"listen-on port 53")
          named[position[0]] = named[position[0]].strip() + self.dns_server_ip.strip() + "; };\n"
          position = self.getPosition(named,"#DIRECT")
          named[position[0]+1] = f'zone "{self.domain_name}" IN '+"{ \n"
          named[position[0]+2] = named[position[0]+2].strip() + f"{self.NStype} ;\n"
          named[position[0]+3] = named[position[0]+3].strip() + f"{self.domain_name} ;\n"
          # self.cmd(f"touch /var/named/{self.domain_name}")
          #REVERSE
          position = self.getPosition(named,"#REVERSE")

          named[position[0]+1] = f'zone "{self.address_riversed}.in-addr.arpa" IN '+"{ \n"
          named[position[0]+2] = named[position[0]+2].strip() + f"{self.NStype} ;\n"
          reversed_domain = self.domain_name.split(".")
          reversed_domain = ".".join(reversed_domain[::-1])
          named[position[0]+3] = named[position[0]+3].strip() + f"{reversed_domain} ;\n"
          # self.cmd(f"touch /var/named/{self.domain_name}")
        with open("Config/dns/named_copy.conf","w") as file :
          file.write("") 
          file.writelines(named)

        with open("Config/dns/header.lab","r") as file :
          header_direct = file.readlines()
          file.seek(0)
          header_inverse =  file.readlines()
        
        position = self.getPosition(header_direct,"SOA")
        print(position)
        header_direct[position[0]] = f"{header_direct[position[0]].strip()} {self.server_hostname}.{self.domain_name}. root.{self.domain_name}. ( \n" 
        header_inverse[position[0]] = f"{header_inverse[position[0]].strip()} {self.server_hostname}.{self.domain_name}. root.{self.domain_name}. ( \n" 

        position = self.getPosition(header_direct,"NS")
        print(position)
        header_direct[position[0]] = f"{header_direct[position[0]].strip()} \t {self.server_hostname}.{self.domain_name}. \n"
        header_inverse[position[0]] = f"{header_inverse[position[0]].strip()} \t {self.server_hostname}.{self.domain_name}. \n"

        position = self.getPosition(header_direct,"IN  A")
        print(position)
        header_direct[position[0]] = f"{header_direct[position[0]].strip()} \t {self.dns_server_ip} \n"
        header_direct.insert(position[0]+1,f"{self.server_hostname}\tIN\tA\t{self.dns_server_ip} \n")
        last_octet = self.dns_server_ip.split(".")
        # header_inverse.insert(position[0],f"{last_octet[-1]}\tIN\tPTR\t{self.server_hostname}.{self.domain_name} \n")
        header_inverse[position[0]] = f"{last_octet[-1]}\tIN\tPTR\t\t{self.server_hostname}.{self.domain_name} \n"


        
        with open(self.direct_zone_PATH,"w") as file :
          file.write("")
          file.writelines(header_direct)
        
        with open(self.reverse_zone_PATH,"w") as file :
          file.write("")
          file.writelines(header_inverse) 

  def ADD_ENTRY(self) : 
    self.init_information()
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

  def cmd(self,command):
    subprocess.run(command,shell=True)

x = DNS()





