import random
import string
import subprocess

class USSER():
  def __init__(self) :
      self.groupNumber = 0
      self.userNumber = 0
      self.groupsName = []
      self.usernames = []
      self.nmbrUsersInGroup = {}
      self.CALLER()
  def create_groups(self):
    print("we are in CREATE_GROUPE stage !!")
    for group in self.groupsName :
      self.cmd(f"groupadd {group}")
      print(f"group {group} has been created successfully !!!")
      pass

  # def create_users(self):

  #   with open("./passwd.txt","r+") as file :
  #     for u in range(self.userNumber) : 
  #       password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
  #       username = f"user{u}"
  #       full_user = f"{username}:{password}"
  #       # self.cmd(f"useradd {username} -G {group}")
  #       # self.cmd(f"echo {username}:{password} | chpasswd ")
  #       file.write(full_user+"\n")



  def informations(self) :
    self.groupNumber = int(input("How many group you want to create ? "))
    self.userNumber = int(input("How many users you want to create ? : "))
    for gn in range(self.groupNumber) : 
      self.groupsName.append(input(f"what the name of the group number {gn+1} : "))
    
    for grpName in self.groupsName :
      self.nmbrUsersInGroup[grpName] = int(input(f"how many user will be in the {grpName} group ? : "))

    print(self.nmbrUsersInGroup)


  def addUsersToGroup(self) :
    # data = []
    print("we are in the ADD_USER stage !!! ")
    N = int(input("how many letter you want to be in the password ? : "))
    with open("./passwd.txt","r+") as file :
      # data = file.readlines()
      i = 0
      for group,nmbr in self.nmbrUsersInGroup.items() :
        for _ in range(nmbr) :
            password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            username = f"user{i}"
            full_user = f"{username}:{password}:{group}"
            self.cmd(f"useradd -G {group} {username} ")
            self.cmd(f"echo {username}:{password} | chpasswd ")
            file.write(full_user+"\n")
            print(f"user {username} has been added SUCCESSFULLY !!!")
          # data[i] = data[i].strip() + f":{group}" + "\n"
          # username = data[i].split(":")[0]
          # self.cmd(f"gpasswd -a {username} {group}")
            i += 1

    # with open("./passwd.txt","w") as file :
    #   file.write("")
    #   file.writelines(data)
    

  def CALLER(self) :
    self.informations()
    self.create_groups()
    # self.create_users()
    self.addUsersToGroup()
    pass

  def cmd(self,command):
    subprocess.run(command,shell=True)

x = USSER()