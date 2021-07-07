import re

class DNS():
  def __init__(self) -> None:
     pass 

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


  def information(self):
    pass








