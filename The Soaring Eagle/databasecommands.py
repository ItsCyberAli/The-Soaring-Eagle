import C2Database




def Deletedatabase():
    C2 = C2Database.ConnectDatabase()
    C2.ClearDatabase()