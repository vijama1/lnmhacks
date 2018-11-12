from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse
<<<<<<< HEAD

=======
from gtts import gTTS
>>>>>>> aman
# extra
import os
import subprocess as sb
import mysql.connector as pysql
<<<<<<< HEAD


def index (request):
	print ('Welcome....')
	return render (request, 'index.html')

def signup (request):
=======
import speech_recognition as sr

import time
def index (request):
	opening_text="Welcome Abord!!"
	opening_voice=gTTS(text=opening_text,lang='en',slow=False)
	opening_voice.save("welcome.mp3")
	os.system("mpg321 welcome.mp3")
	return render (request, 'index.html')

	# print ('Welcome....')


def signup (request):
	opening_text="Please sign up to use the services"
	opening_voice=gTTS(text=opening_text,lang='en',slow=False)
	opening_voice.save("signup.mp3")
	os.system("mpg321 signup.mp3")
>>>>>>> aman
	return render (request, 'signup.html')

def postsignin (request):
	email = request.POST['email']
	password = request.POST['password']
	conn = pysql.connect(user='root',password='m487',database='hadoop',host='localhost')
	if ( conn.is_connected() ):
		cur = conn.cursor()
		query =  ("SELECT * FROM signup "
	                 "WHERE email='{}' and password='{}';".format(email,password) )
		try:
			cur.execute (query)
			fetch = cur.fetchall()
			print (fetch[0])
			request.session['name'] = fetch[0][0]
			if ( len(fetch)>0 ):
				print('Success....')
<<<<<<< HEAD
=======
				opening_text="Hey there, how are you"
				opening_voice=gTTS(text=opening_text,lang='en',slow=False)
				opening_voice.save("loggedin.mp3")
				os.system("mpg321 loggedin.mp3")
>>>>>>> aman
				return render (request, 'success.html')
			else:
				print('invalid....')
				return render (request, 'invalid.html')
<<<<<<< HEAD
	 
		except:
			conn.rollback()
			print("oops..!!")	
=======

		except:
			conn.rollback()
			print("oops..!!")
>>>>>>> aman
			return render (request, 'invalid.html')
	else:
		print ('Something went wrong...')

def postsignup (request):
	name =  request.POST['name']
	email =  request.POST['email']
	contact =  request.POST['contact']
	password =  request.POST['password']
	conn = pysql.connect(user='root',password='m487',host='localhost')
	if ( conn.is_connected() ):
		print ('Database connected successfully...')
		cur = conn.cursor()
		cur.execute ("""create database if not exists hadoop""")
		cur.execute ("use hadoop")
<<<<<<< HEAD
		cur.execute ("""create table if not exists signup (  
=======
		cur.execute ("""create table if not exists signup (
>>>>>>> aman
						name CHAR(20) NOT NULL,
						email CHAR(30) NOT NULL PRIMARY KEY,
						contact BIGINT UNSIGNED NOT NULL,
						password CHAR(15) NOT NULL )""")
		query = ("INSERT INTO signup "
	          "(name, email, contact, password) "
	          "VALUES ('%s','%s','%d','%s')" % (name, email, int(contact), password) )
		try:
			cur.execute(query)
			conn.commit()
			message = ' Account created successfully'
			return render (request, 'index.html', {'message': message})
		except:
			conn.rollback()
			print("oops..!!")
	else:
		print ('Something went wrong...')
		message = 'Something went wrong'
		return render (request, 'signup.html', {'message': message})

def dashboard (request):
<<<<<<< HEAD
	print ('Dashboard is here...............')
=======

>>>>>>> aman
	container_name = request.session.get('container_name')
	vm = request.session.get('vm')

	print (vm)

<<<<<<< HEAD
	if ( container_name == None and vm == None):
		request.session['client'] = None
		no_cluster = "No Cluster"
		request.session['no_cluster'] = no_cluster
		return render (request, 'dashboard.html', {'no_cluster':no_cluster})

	elif (container_name == None and vm == 'vm'):
		ip_list = request.session.get('ip_list')
		service_provided = request.session.get('service_provided')	
		service_status = request.session.get('service_status')	
		all_details = zip(ip_list,service_provided,service_status)
		request.session['no_cluster'] = 'cluster_existed'
		vm = "VM based Cluster"
		print(vm)
		return render (request, 'dashboard.html', {'vm':vm , 'all_details':all_details })

	else:                                                                                              #-- Everything works fine
		index_value = request.session.get('index_value')
		service_type = request.session.get('service_type')
		container_id = request.session.get('container_id')
		ip_list = request.session.get('ip_list')
		container_type = request.session.get('container_type')
		service_status = request.session.get('service_status')
		request.session['no_cluster'] = 'cluster_existed'
		docker = "docker"
		all_details = zip(index_value,container_name,ip_list,container_id,container_type,service_status)
		return render (request, 'dashboard.html',
			{'all_details':all_details ,'docker':docker,'service_type':service_type})
=======


	try:

		if ( container_name == None and vm == None):
			request.session['client'] = None
			no_cluster = "No Cluster"
			request.session['no_cluster'] = no_cluster
			print("hello")
			return render (request, 'dashboard.html', {'no_cluster':no_cluster})

		elif (container_name == None and vm == 'vm'):
			ip_list = request.session.get('ip_list')
			service_provided = request.session.get('service_provided')
			service_status = request.session.get('service_status')
			all_details = zip(ip_list,service_provided,service_status)
			request.session['no_cluster'] = 'cluster_existed'
			vm = "VM based Cluster"
			print("hello")
			print(vm)
			return render (request, 'dashboard.html', {'vm':vm , 'all_details':all_details })


		else:                                                                                              #-- Everything works fine
			index_value = request.session.get('index_value')
			service_type = request.session.get('service_type')
			container_id = request.session.get('container_id')
			ip_list = request.session.get('ip_list')
			container_type = request.session.get('container_type')
			service_status = request.session.get('service_status')
			request.session['no_cluster'] = 'cluster_existed'
			docker = "docker"
			print("hello")
			all_details = zip(index_value,container_name,ip_list,container_id,container_type,service_status)
			return render (request, 'dashboard.html',
				{'all_details':all_details ,'docker':docker,'service_type':service_type})

	finally:
		# time.sleep(5)
		text=""
		print("hello")
		opening_text="Dashboard is here"
		opening_voice=gTTS(text=opening_text,lang='en',slow=False)
		opening_voice.save("dashboard.mp3")
		os.system("mpg321 dashboard.mp3")
		print ('Dashboard is here...............')
		creating_message="say"
		voice=gTTS(text=creating_message,lang='en',slow=False)
		voice.save("cluster_ask.mp3")
		os.system("mpg321 cluster_ask.mp3")
		print("say")
		try:
			r=sr.Recognizer()
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				audio=r.listen(source)
				text=r.recognize_google(audio)
				print("you said: "+text)
		except:
			# return render(request,'dashboard.html')
			if ( container_name == None and vm == None):
				request.session['client'] = None
				no_cluster = "No Cluster"
				request.session['no_cluster'] = no_cluster
				print("hello")
				return render (request, 'dashboard.html', {'no_cluster':no_cluster})

			elif (container_name == None and vm == 'vm'):
				ip_list = request.session.get('ip_list')
				service_provided = request.session.get('service_provided')
				service_status = request.session.get('service_status')
				all_details = zip(ip_list,service_provided,service_status)
				request.session['no_cluster'] = 'cluster_existed'
				vm = "VM based Cluster"
				print("hello")
				print(vm)
				return render (request, 'dashboard.html', {'vm':vm , 'all_details':all_details })


			else:                                                                                              #-- Everything works fine
				index_value = request.session.get('index_value')
				service_type = request.session.get('service_type')
				container_id = request.session.get('container_id')
				ip_list = request.session.get('ip_list')
				container_type = request.session.get('container_type')
				service_status = request.session.get('service_status')
				request.session['no_cluster'] = 'cluster_existed'
				docker = "docker"
				print("hello")
				all_details = zip(index_value,container_name,ip_list,container_id,container_type,service_status)
				return render (request, 'dashboard.html',
					{'all_details':all_details ,'docker':docker,'service_type':service_type})
		finally:
			if "cluster" in text.strip():
				return render (request, 'service.html')
		# 		# if "create new cluster"
>>>>>>> aman

def service_status (request):
	service_status = request.session.get('service_status')
	reference_var = request.GET['reference_var']
	index = int(request.GET['index'])
	service_type = request.GET['type']
	service_type = service_type.split('&')
	if (len(service_type) == 1):
<<<<<<< HEAD
		if (service_status[index] == 'Running'): 
=======
		if (service_status[index] == 'Running'):
>>>>>>> aman
			os.system('sudo docker exec '+reference_var+' hadoop-daemon.sh stop '+service_type[0])
			service_status[index] = 'Stopped'
		else:
			os.system('sudo docker exec '+reference_var+' hadoop-daemon.sh start '+service_type[0])
			service_status[index] = 'Running'
	else:
		print(service_type)
		print('two')
	print (service_status)
	request.session['service_status'] = service_status
	return redirect ('/dashboard/')

def about (request):
	return render (request, 'about.html')

def create (request):
<<<<<<< HEAD
=======
	opening_text="Create your new cluster here"
	opening_voice=gTTS(text=opening_text,lang='en',slow=False)
	opening_voice.save("cluster.mp3")
	os.system("mpg321 cluster.mp3")
>>>>>>> aman
	return render (request, 'service.html')

def settings (request):
	return render (request, 'settings.html')
<<<<<<< HEAD



=======
>>>>>>> aman
