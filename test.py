

with open("./Config/dhcp/add.txt","r") as file :
  origin = file.readlines()
newlist = []
print(len(origin)-1)
for n,i in enumerate(origin) :
    newlist.append(i.strip() + " " +str(n))
    print(n)
  

print(origin)
print(newlist)
