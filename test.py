import re

# with open("./Config/dhcp/try.txt","r") as file :
#   origin = file.readlines()

# the_Ligne_number = 0
# for n,i in enumerate(origin) :
#     founded = re.search("client2",i)
#     if str(founded) != "None" :
#       print(founded)
#       the_Ligne_number = n
#       break

# print(the_Ligne_number)
with open("./passwd.txt","r") as file :
  origin = file.readlines()

for i in range(len(origin)-1) :
  origin[i] = origin[i].strip() + f":group"
  print(origin[i].split(":")[0])
print(len(origin))