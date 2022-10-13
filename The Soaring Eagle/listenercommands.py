
#from unittest import result
from keyboard import press
import C2Database, color
from tabulate import tabulate
import httplistener
import sqlite3
from keyboard import press



def CreateListener():
        C2 = C2Database.ConnectDatabase()
        listenername = input(color.yellow("\n[+] What is the name of the listener you want to create: "))
        port = int(input(color.cyan("[+] What is the port number you want the listener to operate on: ")))
        ipaddress = input(color.green("[+] What is the IP address of the listener: "))
        listenertype = input(color.red("[+] What type of listener is this (You Can Put Anything But Put HTTP): "))
        C2.CreateListener(listenername, ipaddress, port, listenertype)
        print((color.green("\n[+]The Following Listener {} Has Been Created!\n")).format(listenername), color.cyan("[-] Listener Name: {}\n").format(listenername), color.blue("[-] IP Address: {}\n".format(ipaddress)), color.yellow("[-] Port: {}\n".format(port)))
        #print("\nThe Following Listener Has Been Created:\nListenerName: {} IpAddress: {} Port: {}".format(color.red(listenername), color.green(ipaddress), color.yellow(str(port))))

def ListListeners():
        C2 = C2Database.ConnectDatabase()
        results = C2.ListListener()
        print("\n",tabulate(results, headers=[color.red("Listener Name"), color.green("Listener IP"), color.yellow("Listener Port")]),"\n")

def ListImplants():
        C2 = C2Database.ConnectDatabase()
        results = C2.ListImplants()
        print("\n",tabulate(results, headers=[color.red("Implant Name"), color.green("Key"), color.yellow("Listener Name"), color.yellow("Listener IP"), color.yellow("Listener Port")]),"\n")

def DeleteListeners():
    ListListeners()    
    listenername = input(color.green("[+] What is the name of the listener you want to delete?: "))
    C2 = C2Database.ConnectDatabase()
    results = C2.DeleteListener(listenername)
    print(color.yellow("[+]"), color.red("The Following Listener Named {} has been deleted \n").format(listenername))
    return results

def StartIt():
    connect = sqlite3.connect("C2Database.db")
    ListListeners()
    print(color.yellow("[+]"),color.green("Please Make Sure You Type The Correct Name Of The Listener Or Else It Will Make You Create A New Listener! (Case Sensitive) \n"))
    listenername = input(color.red("[+] What is the name of the listener you want to start: "))
    results = connect.execute("SELECT ListenerIPAddress, ListenerPort FROM Listeners WHERE ListenerName='%s'" % listenername)
    results = results.fetchall()
    try:
                listener_ip = results[0][0]
                port = results[0][1]
                 
    except:
                print(color.yellow("\n[+]"),color.green("Creating A New Listener Because The Listener Name You Entered Was Incorrect (Please Continue Or Else The Program Will Crash)"))
                listenername = input(color.blue("\n[+] What is the name of the listener you want to start: "))
                listener_ip = input(color.yellow("[+] What is the ip address of the listener you want to start: "))
                port = input(color.green("[+] What is the port number you want the listener to operate on: "))

    httplistener.Start(listener_ip, port)
    print(color.green("\n[+]"),color.cyan("The Following Listener {} Has Started & Is Operating At http://{}:{} (Listener Has Only Started But Not Created Nor Saved In The Database) \n").format(listenername, listener_ip, port))
