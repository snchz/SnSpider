from urllib.request import urlopen
import re, datetime

class SnSpider:
 def __init__(self,url):
  f=f=urlopen(url)
  self.datos=str(f.read())
 def obtenerContenidoURL(self):
  return self.datos
 def buscarPor(self,patron):
  return re.findall(patron,self.datos)
 def contiene(self,texto):
  if texto in self.datos:
   return True
  else:
   return False
