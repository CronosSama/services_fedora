import re



class DHCP():

  def __init__(self,option) -> None:
      self.inputs = []
      self.option = option
      self.how_much_ligne = 0
      self.configPATH = "/etc/dhcp/dhcpd.conf"
      self.CALLER()
      

  def CALLER(self) :
  # self.PATH = "/etc/dhcp/dhcpd.conf"
    
    if re.search("ADD",self.option) != None :
      if self.option == "ADD_NETWORK" :
        self.inputs = ["subnet","netmask","range","dns-server","domain-name","default-gateway","broadcast-address","default-lease-time","max-lease-time"]
        self.PATH = "./Config/dhcp/add.txt"

      
      if self.option == "ADD_FIXED" :
        self.inputs = ["hostname","hardware ethernet","fixed-address"]
        self.PATH = "./Config/dhcp/fixed.txt"
    
      self.ADDER()
      return "Awaited"



    elif re.search("REMOVE",self.option) != None :
      if self.option == "REMOVE_FIXED" :
        self.how_much_ligne = 4

      elif self.option == "REMOVE_NETWORK" :
        self.how_much_ligne = 9
        
      self.REMOVER()
    


  def ADDER(self) :

      conf = []

      #just tanjm3 les valeur li hanzid
      for inp in self.inputs :
        new = input(f"the value of {inp} : ")
        conf.append(new)
      origin = []

      with open(self.PATH,"r") as file :
        origin = file.readlines()

      for i,data in enumerate(conf) :
        if i == 0 and self.option == "ADD_NETWORK" :
          origin[i] = "subnet "+conf[i]+" netmask "+conf[i+1]+" {\n"
          continue
        if i == 0 and self.option == "ADD_FIXED" :
          origin[i] = "host "+conf[i] +"{\n"
          continue
        if i == 1 and self.option == "ADD_NETWORK" :
          pass

        else : 
          if self.option == "ADD_NETWORK" :
            i = i-1

          origin[i]=origin[i].strip()
          origin[i] = origin[i]+" "+data+" ;\n"

      origin[len(origin)-1] = "} \n"
      with open(self.configPATH,"r") as file :
        old = file.readlines()
      with open(self.configPATH,"w") as file :
        if self.option == "ADD_NETWORK" :
          file.writelines(origin+old)
        else :
          file.writelines(old+origin)





    #self.cmd("cp /usr/share/doc/dhcp-server/dhcpd.conf.example /etc/dhcp/dhcpd.conf")

  def REMOVER(self) : 
    searched_word = input("what are you looking for  ? ")


    with open(self.configPATH,"r") as file :
      origin = file.readlines()

    the_Ligne_number = 0
    for n,i in enumerate(origin) :
        founded = re.search(searched_word,i)
        if str(founded) != "None" :
          the_Ligne_number = n
          break

    for ligne in range(self.how_much_ligne) : 
      origin[the_Ligne_number + ligne] = ""

    with open(self.configPATH,"w") as file :
      file.writelines(origin)


















