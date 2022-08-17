import random

serverDiensteList = ["Web Server", "E-Mail Server", "FTP Server"]
hardwareServerList = []
currentServerID = -1

#Aufgabe 2
def serverDienste():
    i = 0
    serverVerfugbar = []
    print("\nMonitoring - Programme \n====================== \n\nLister der vorhandenen Server-Dienste:\n")
    while (len(serverDiensteList) > i):
        serverVerfugbar.append(random.randint(0, 1))
        print(str(i + 1) + ". " + str(serverDiensteList[i]) + " (" + str(numberToStatus(serverVerfugbar[i])) + ")")
        i += 1
    print("\nIngesamt existieren " + str(len(serverDiensteList)) + " Server-Dienste.\n")
    
def numberToStatus(i):
    if(i == 0):
        return "Online"
    if(i == 1): 
        return "Offline"    

#Aufgabe 3
def addHardwareServer(s, list):
    global hardwareServerList  
    temp = checkList(list)
    if(checkServerName(s) is True):
        if(len(hardwareServerList) == 0):
            hardwareServerList.append([s, temp])  
            printAddedServer(s, temp)   
        elif(checkDuplicateServer(s) is False):  
            hardwareServerList.append([s, temp])
            printAddedServer(s, temp)              
      
def checkDuplicateServer(s):
    global currentServerID
    i = 0
    exists = False
    while(i < len(hardwareServerList)):
        if(hardwareServerList[i][0] != s and exists is False):
            i += 1
        else: 
            exists = True
            currentServerID = i
            break
    return exists
          
                  
def printAddedServer(s, temp):
    print("Hardware Server " + s + " wurde hinzugefügt mit folgenden Diensten: ", end="")
    j = 0
    while(j < len(temp)):
        if(j + 1 < len(temp)):
            print(temp[j], end=", ")
        else: 
            print(temp[j], end=".\n")
        j += 1                        

def checkList(list):
    temp = []
    i = 0
    while(i < len(list)):
        j = 0
        while(j < len(serverDiensteList)):
            if(list[i] == serverDiensteList[j]):
                temp.append(serverDiensteList[j])
            j += 1
        i += 1
    return temp

def checkServerName(s):
    isAllowed = False
    if(s[0] == "S" and s[1] == "N"):
        i = 2
        temp = ""
        while(i < len(s)): 
            temp += str(s[i])
            i += 1
        if(int(temp) < 6501 and int(temp) > 0):
            isAllowed = True
    return isAllowed

def updateServer(s, list):
    global currentServerID, hardwareServerList
    currentServerID = -1
    if(checkDuplicateServer(s) is True):
        temp = checkList(list)
        hardwareServerList[currentServerID] = (s, temp)
        print("Die Dienste des Servers " + s + " wurden geändert zu: ", end="")
        j = 0
        while(j < len(temp)):
            if(j + 1 < len(temp)):
                print(temp[j], end=", ")
            else: 
                print(temp[j], end=".\n")
            j += 1
    else:
        print("Server " + s + " wurde nicht gefunden!")
        
def deleteServer(s):
    global currentServerID, hardwareServerList
    currentServerID = -1
    if(checkDuplicateServer(s) is True):
        del hardwareServerList[currentServerID] 
        print("Hardware Server " + s + " wurde erflogreich gelöscht!")
    else:
        print("Server " + s + " wurde nicht gefunden!")
        
    
    

serverDienste()
addHardwareServer("SN5002", ["Web Server", "Datenbank Server"])
addHardwareServer("SN0342", ["FTP Server", "Web Server"])
addHardwareServer("SN0342", ["FTP Server", "Web Server"])
updateServer("SN5002", ["FTP Server"])
deleteServer("SN0342")
duplicate = checkDuplicateServer("SN5002")
print(duplicate)