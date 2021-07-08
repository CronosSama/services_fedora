# import re
from re import sub
import subprocess
# import colorama
# from colorama import Fore,Back,Style
# # import time 
# # from threading import Thread
# # from multiprocessing import Pool

# # def func(n):
# #   print(f"func {n} : STARTING ....")
# #   d = 0
# #   while d < 500000000:
# #     d += 1
# #   print(f"func {n} : FINISHED ....")

# # # t_1 = Thread(target=func,args=([1]))
# # # t_2 = Thread(target=func,args=([2]))
# # pool = Pool(processes=2)
# # start = time.time()
# # print("i started here")


# # r1 = pool.apply_async(func,[1])
# # r1 = pool.apply_async(func,[2])
# # pool.close()
# # pool.join()
# # # t_1.start()
# # # t_2.start()
# # # t_1.join()
# # # t_2.join()
# # finish = time.time()

# # print(f"finished in : { finish - start } ")




# # # with open("./Config/dhcp/try.txt","r") as file :
# # #   origin = file.readlines()

# # # the_Ligne_number = 0
# # # for n,i in enumerate(origin) :
# # #     founded = re.search("client2",i)
# # #     if str(founded) != "None" :
# # #       print(founded)
# # #       the_Ligne_number = n
# # #       break

# # # print(the_Ligne_number)
# # # with open("./passwd.txt","r") as file :
# # #   origin = file.readlines()

# # # for i in range(len(origin)-1) :
# # #   origin[i] = origin[i].strip() + f":group"
# # #   print(origin[i].split(":")[0])
# # # print(len(origin))
# # lol = []
# with open("./Config/dns/named_copy.conf","r") as file :
#   lol = file.readlines()

# # find_start = 0
# # find_end   = 0


# def test(file,first,end=False) :
#   #daba plan wmafih anaho ana tan9lb 3la wa7d l3iba tatbda bchi l3iba "first"
#   # had l3iba tatkml bchi l3iba okhra tanprovidiha f "end", w brit index fin taykml 7ta howa 
#   # tandiro return wa7d array fih index dyal lbdya wdyal nihaya
#   # 
 
#   array = []
#   for index,item in enumerate(file) :

#     search = re.search(first,item)
#     if search != None : 
#       array.append(index)
#       #hadi drtha bach mnin yl9a hadak first wtan7to index dyalo
#       #nnbdlo valeur dyal first b valeur dyal end bach y9lb 3liha
#       #blast mandiro wa7d for loop okhra wla variable okhra
#       first = end
#       #hadi mnin yl9a dakchi li khasni fi 7alat 3tito first w end safi critiria lwla hatkhdm w ytra loop break
#       #tanya hiya fi7alat tansearchi her 3la index dyal chi kalma wla jomla safi wmam7tajch end
#     if len(array) == 2 or (len(array) == 1 and end == False) :
#       break
#   return array

# # position = test(lol,"acl","}")
# # lol.insert(position[0]+1,"JAJAJA")

# # position = test(lol,"#DIRECT")
# # print(lol[position[0]])
# # print(lol[position[0]+1])
# # print(lol[position[0]+2])
# # print(lol[position[0]+3])


# named = "sen.netmobo.lab"
# named = named.split(".")
# print(".".join(named[::-1]))
# # print(lol)

# # result = test(lol,"listen-on port")
# # print(result)

# # with open("./Config/dns/named_copy.conf","w") as file :
# #   file.writelines(lol)


# # print(lol)




interface = subprocess.run("ifconfig | head -1 | cut -d: -f1",shell=True,capture_output=True)

print(interface.stdout.decode().strip())











