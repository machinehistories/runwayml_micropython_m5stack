from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
import urequests
import time
import json
import base64 #install python library
from numbers import Number

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x387f98)


x = None
y = None
url = None
output = None
img = None
headers = None
inputs = None
status = None
size = None
neuron = None
runway_set = None

wifiCfg.doConnect('<uuid>', ',password>')
label0 = M5Label('', x=224, y=25, color=0x000, font=FONT_UNICODE_24, parent=None)
label1 = M5Label('text', x=0, y=217, color=0x000, font=FONT_UNICODE_24, parent=None)
label0.set_hidden(True)
if wifiCfg.wlan_sta.isconnected():
  label0.set_text('wifi ok')
wait(5)
label0.set_text('')
size = 320


# Describe this function...
def runway(x, y):
  global url, output, img, headers, inputs, status, size, neuron, runway_set
  url = 'https://<runway-ml-model>.hosted-models.runwayml.cloud/v1/query'
  headers = {'Accept':'application/json','Content-Type':'application/json','Authorization':'Bearer <your id>'}
  inputs = {'layer':'maxpool4 (max:480)','neuron':x,'size':y,'transforms':False,'transform_min':0.1,'transform_max':0.5}
  try:
    req = urequests.request(method='POST', url=url,json=inputs, headers=headers)
  except:
    status = req.status_code
    label1.set_text(str(status))
  output = json.loads((req.text))
  return output

# Describe this function...
def format_image():
  global x, y, url, output, img, headers, inputs, status, size, neuron, runway_set
  img = output['image']
  img = img.replace('data:image/jpeg;base64,', '')
  imgdata = base64.b64decode(img)
  lcd.image_buff(lcd.CENTER, lcd.CENTER, imgdata)
  label1.set_text(str((str('neuron:') + str(neuron))))




while True:
  neuron = (neuron if isinstance(neuron, Number) else 0) + 1
  runway_set = runway(neuron, size)
  format_image()
  wait_ms(2)
