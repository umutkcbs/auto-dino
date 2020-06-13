import time
import http.server
import socketserver
from threading import Thread
from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome('chromedriver.exe')

keyboard = Controller()

#burada biyerlere while true koycam
#veriyi cek 

    
PORT = 4444
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("localhost", PORT), Handler)

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
driver.get('http:/www.google.com')
print('buraya geldi')

print("serving at port", PORT)

###########################################
def sayfa():
    driver.get('path to file')

def basla():
    httpd.serve_forever()

def zipla(): 
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    
if __name__ == "__main__":
    Thread(target= basla).start()
    Thread(target= sayfa).start()
    time.sleep(3)
    while True:
        aa = driver.get_log('browser')
        aaa = str(aa)
        if 'kaktus' in aaa:
            zipla()
        else:
            continue
            
#HATALI DÜZELTMEM GEREKİYOR