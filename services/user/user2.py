import random
import string
import subprocess

# from multiprocessing import Pool
import time
class USERCHANGER():
  def __init__(self) :
      self.groupNumber = 0
      self.userNumber = 0
      self.passwordLength = 0
      self.groupsName = []
      self.usernames = []
      self.All_Group_Info = []
      self.arrayOfNumber = []
      self.CALLER()


  def informations(self) :
    self.groupNumber = int(input("How many Group exists ? "))
    self.userNumber = int(input("How many users exists ? : "))
    # self.passwordLength = int(input("how many letter you want to be in the password ? : "))
    for gn in range(self.groupNumber) : 
      self.groupsName.append(input(f"what the name of the group number {gn+1} : "))
    count = 0
    for grpName in self.groupsName :
      nmb = int(input(f"how many user in the {grpName}  : "))
      obj = {}
      obj["name"] = grpName
      obj["unum"] = nmb
      obj["starter"] = count
      self.All_Group_Info.append(obj)
      count += nmb
    print(self.All_Group_Info)


  def addUsersToGroup(self,One_Group_INFO) :
    group = One_Group_INFO["name"]
    
    print(f"we are in the ADD_USER stage for group : { group } !!! ")

    # self.cmd(f"touch ./groups/{group}.txt")
    # self.cmd(f" groupadd {group}")
    # with open(f"./groups/{group}.txt","r+") as file :
    # i = One_Group_INFO["starter"]
    password = ""
    if group == "1BAC" : 
      password = "bac1"
    elif group == "2BAC" : 
      password = "bac2"
    elif group == "TC" :
      password = "tronc"
    i=1
    for _ in range(One_Group_INFO["unum"]) :
        # password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.passwordLength))
        username = f"{group}-Poste{i}"

        # full_user = f"{username}:{password}:{group}"
        self.cmd(f"usermod -l {username.lower()} {username}")
        # self.cmd(f"echo {username}:{password} | chpasswd ")
        # option e for echo can interept \n not write it
        #comment thiisisisisisisisisisisisisisi
        self.cmd(f'echo -e "{password}\n{password}" | passwd {username.lower()} ')
        self.cmd(f"smbpasswd -x {username}")

        self.cmd(f'echo -e "{password}\n{password}" | smbpasswd -as {username.lower()} ')
        # self.cmd(f'mkdir /share/{group}/{username} ; chmod 707 /share/{group}/{username} ;chown {username}:{group} /share/{group}/{username} ')
        # # self.cmd(f"./ip.sh {username} {password} {group}")
        # file.write(full_user+"\n")
        print(f"user {username} has been changed to {username.lower()} SUCCESSFULLY !!!")
        i += 1

  def CALLER(self) :
    self.informations()
    self.cmd(f"mkdir ./groups") 
    # pool = Pool(processes=len(self.All_Group_Info))
    start = time.time()
    for One_Group_INFO in self.All_Group_Info : 
      # process = pool.apply_async(self.addUsersToGroup,[One_Group_INFO])
      self.addUsersToGroup(One_Group_INFO)
      print("wait i'am finished already ? wtf ")
    # pool.close()
    # pool.join() 
      
    end = time.time()
    print(f"it tooks {end - start} to whole things done .... ")
  def cmd(self,command):
    subprocess.run(command,shell=True)

x = USERCHANGER()