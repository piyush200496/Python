from flask import Flask, render_template, request
from pymongo import MongoClient
import gridfs
import cognitive_face as CF
import json
from os.path import join, dirname,abspath
from PIL import Image, ImageDraw



app=Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method=='POST':
		age=request.form['age']
		name=request.form['name']
		imgname=request.form['imgname']
		print(age)
		print(name)
		print(imgname)
		insert_rec(age,name,imgname)
		return render_template('output.html',name=name,age=age)
	return render_template('info.html')	

def getval(k,l):
	for d in l:
		if k in d:
			 return d[k]

def face_recog(imgname):
	KEY = '60228c30ff494e188cac455517af5a50'  # Replace with a valid Subscription Key here.
	CF.Key.set(KEY)

	BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
	CF.BaseUrl.set(BASE_URL)
	img_url = join('../py/images',imgname)
#img_url='img.png'
	result = CF.face.detect(img_url)
	print(result)
	y=getval('faceRectangle',result)
	print(y)
	t=y['top']
	l=y['left']
	h=y['height']
	w=y['width']
	r=t+w
	b=l+h
	pic=Image.open(img_url)
	pict=pic.crop((l,t,b,r))
	modified_file=join('../py/modified',imgname)
	pict.save(modified_file)
	return modified_file


def insert_rec(age,name,imgname):
	mongodb_uri="mongodb://test:test@ds012178.mlab.com:12178/mydb"
	client= MongoClient(mongodb_uri, connectTimeoutMS=30000)
	db=client.get_database("mydb")
	##filename=join('../py/images',imgname)
	url=face_recog(imgname)
	with open(url,'rb') as p:
		thedata=p.read()
	fs=gridfs.GridFS(db)
	stored=fs.put(thedata,filename=name)
	pi=db.patient_info
	rec={"name":name, "age":age}
	pi.insert_one(rec)
	
	#outputdata=fs.get(stored).read()

@app.route('/rec',methods=['GET','POST'])
def rec():
	if request.method=='POST':
		repname=request.form['repname']
		mongodb_uri="mongodb://test:test@ds012178.mlab.com:12178/mydb"
		client= MongoClient(mongodb_uri, connectTimeoutMS=30000)
		db=client.get_database("mydb")
		val=db.patient_info.find({"name":repname}).count()>0
		if val:
			print(val)
			fs=gridfs.GridFS(db)
			outputdata=fs.get_version(filename=repname).read()
			repname=repname+'.jpg'
			outfilename=join('../py/imagesoutput/',repname)
			output=open(outfilename,'wb')
			output.write(outputdata)	
			return render_template('success.html')
		
			output.close()
		else:
			return render_template('fail.html')	
	return render_template('test_cred.html')
	#mongodb_uri="mongodb://test:test@ds012178.mlab.com:12178/mydb"
	#client= MongoClient(mongodb_uri, connectTimeoutMS=30000)
	#db=client.get_database("mydb")
	#fs=gridfs.GridFS(db)
	#outputdata=fs.get_version(filename="gdf").read()
	#outfilename=join('../py/imagesoutput/',"gdf.jpg")
	#output=open(outfilename,'wb')
	#output.write(outputdata)	
	#output.close()
#an #output folder needs to be created in py directory



if __name__=="__main__":
	app.run()		
