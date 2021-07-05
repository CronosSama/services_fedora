import random
import string
import subprocess
from multiprocessing import Pool
import time
class USSER():
  def __init__(self) :
      self.groupNumber = 0
      self.userNumber = 0
      self.passwordLength = 0
      self.groupsName = []
      self.usernames = []
      self.All_Group_Info = []
      self.arrayOfNumber = []
      self.CALLER()


  def create_groups(self):
    print("we are in CREATE_GROUPE stage !!")
    for group in self.groupsName :
      
      print(f"group {group} has been created successfully !!!")
      


  def informations(self) :
    self.groupNumber = int(input("How many group you want to create ? "))
    self.userNumber = int(input("How many users you want to create ? : "))
    self.passwordLength = int(input("how many letter you want to be in the password ? : "))
    for gn in range(self.groupNumber) : 
      self.groupsName.append(input(f"what the name of the group number {gn+1} : "))
    count = 0
    for grpName in self.groupsName :
      nmb = int(input(f"how many user will be in the {grpName} group ? : "))
      obj = {}
      obj["name"] = grpName
      obj["unum"] = nmb
      obj["starter"] = count
      self.All_Group_Info.append(obj)
      count += nmb
    print(self.All_Group_Info)


  def addUsersToGroup(self,One_Group_INFO,c) :
    group = One_Group_INFO["name"]
    
    print(f"we are in the ADD_USER stage for group : { group } !!! ")

    self.cmd(f"touch ./groups/{group}.txt")
    self.cmd(f"groupadd {group}")
    with open(f"./groups/{group}.txt","r+") as file :
      i = One_Group_INFO["starter"]
      # for One_Group_INFO in self.All_Group_Info :
      for _ in range(One_Group_INFO["unum"]) :
          password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.passwordLength))
          username = f"user{i}"
          full_user = f"{username}:{password}:{group}"
          self.cmd(f"sudo useradd -G {group} {username} ;  chpasswd {username}:{password} ")
          file.write(full_user+"\n")
          print(f"user {username} has been added SUCCESSFULLY !!!")
          i += 1

  def CALLER(self) :
    self.informations()
    self.cmd(f"mkdir ./groups") 
    pool = Pool(processes=len(self.All_Group_Info))
    start = time.time()
    for c,One_Group_INFO in enumerate(self.All_Group_Info) : 
      process = pool.apply_async(self.addUsersToGroup,[One_Group_INFO,c])
      print("wait i'am finished already ? wtf ")
    pool.close()
    pool.join() 
      
    end = time.time()
    print(f"it tooks {end - start} to whole things done .... ")
  def cmd(self,command):
    subprocess.run(command,shell=True)

x = USSER()