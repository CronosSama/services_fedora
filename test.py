import re
import time 
from threading import Thread
from multiprocessing import Pool

def func(n):
  print(f"func {n} : STARTING ....")
  d = 0
  while d < 500000000:
    d += 1
  print(f"func {n} : FINISHED ....")

# t_1 = Thread(target=func,args=([1]))
# t_2 = Thread(target=func,args=([2]))
pool = Pool(processes=2)
start = time.time()
print("i started here")


r1 = pool.apply_async(func,[1])
r1 = pool.apply_async(func,[2])
pool.close()
pool.join()
# t_1.start()
# t_2.start()
# t_1.join()
# t_2.join()
finish = time.time()

print(f"finished in : { finish - start } ")




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
# with open("./passwd.txt","r") as file :
#   origin = file.readlines()

# for i in range(len(origin)-1) :
#   origin[i] = origin[i].strip() + f":group"
#   print(origin[i].split(":")[0])
# print(len(origin))