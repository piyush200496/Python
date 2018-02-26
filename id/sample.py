import cognitive_face as CF
import json
from os.path import join, dirname,abspath
from PIL import Image, ImageDraw
def getval(k,l):
	for d in l:
		if k in d:
			 return d[k]


KEY = '60228c30ff494e188cac455517af5a50'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
img_url = 'img.jpg'
#img_url='img.png'
result = CF.face.detect(img_url)
print(result)
x=json.dumps(result)
data=json.loads(x)
#print("success")
y=getval('faceRectangle',result)
print(y)
#print(left)
t=y['top']
l=y['left']
h=y['height']
w=y['width']
r=t+w
b=l+h
pic=Image.open("img.jpg")
pict=pic.crop((l,t,b,r))
pict.save("modified.jpg")