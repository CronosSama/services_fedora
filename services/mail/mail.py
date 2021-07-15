
####Installation#
# dnf -y install postfix
# dnf -y install dovecot
# dnf -y install mailx
# 
# 
# 
# #

class Mail():
  def __init__(self,domain_name,hostname,network_address,prefix) -> None:

      self.domain_name = domain_name
      self.hostname = hostname
      self.network_address = network_address
      self.prefix = prefix
      self.server_config_file_1 = "/etc/postfix/main.cf"
      self.arrayOfLinks = ["dovecot.conf",
                           "conf.d/10-mail.conf",
                           "conf.d/10-master.conf",
                           "conf.d/10-ssl.conf"
                           ]


      self.configuration_postfix()
      self.configuration_dovecot()

  def configuration_postfix(self) : 
    with open("Config/mail/main.cf","r") as file : 
      file_array = file.readlines()

    file_array[94] = file_array[94].strip() + f" {self.hostname}.{self.domain_name} \n"
    file_array[101] = file_array[101].strip() + f" {self.domain_name} \n"
    file_array[282] = file_array[282].strip() + f" {self.network_address}/{self.prefix} \n"

    with open(self.server_config_file_1,"w") as file : 
      file.write("")
      file.writelines(file_array)

  def configuration_dovecot(self) :
    for fileName in self.arrayOfLinks : 
      with open(f"Config/mail/{fileName}","r") as file :
        original = file.readlines()

      with open(f"/etc/dovecot/{fileName}","w") as file :
        file.write(" ")
        file.writelines(original)

    