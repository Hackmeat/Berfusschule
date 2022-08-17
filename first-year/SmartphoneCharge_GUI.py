from tkinter import *

def setupViews():
    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    
    rbuttonProvider1.grid(row=3)
    rbuttonProvider2.grid(row=4)
    rbuttonProvider3.grid(row=5)
    rbuttonProvider4.grid(row=6)
    
    rbuttonGuthaben1.grid(row=3, column=1)
    rbuttonGuthaben2.grid(row=4, column=1)
    rbuttonGuthaben3.grid(row=5, column=1)
    
    button1.grid(row=6, column=1)
    
#Checking numbers
def checkNumber():
    num1 = entry1.get()
    num2 = entry2.get()
    checkRadio1 = provider.get()
    checkRadio2 = guthaben.get()
    if ((num1 == num2) and (checkRadio1 > 0) and (checkRadio2 > 0)):
        label3.config(text="Erfolgreich")
    else:
        if(num1 != num2):
            entry2.delete(0, END)
            label3.config(text="Falsche Nummer")
        else:
            label3.config(text="Falsche Auswahl")   

root = Tk()

#Add labels
label1 = Label(root, text="Handynummer")
label2 = Label(root, text="Wiederholung")
label3 = Label(root, text="")

#Add entry
entry1 = Entry(root)
entry2 = Entry(root)

#Add radiobutton
provider = IntVar()
guthaben= IntVar()

rbuttonProvider1 = Radiobutton(root, text="FYVE", padx = 20, variable=provider, value=1)
rbuttonProvider2 = Radiobutton(root, text="BLAU", padx = 20, variable=provider, value=2)
rbuttonProvider3 = Radiobutton(root, text="KLAR", padx = 20, variable=provider, value=3)
rbuttonProvider4 = Radiobutton(root, text="BASE", padx = 20, variable=provider, value=4)

rbuttonGuthaben1 = Radiobutton(root, text="15", padx = 20, variable=guthaben, value=15)
rbuttonGuthaben2 = Radiobutton(root, text="20", padx = 20, variable=guthaben, value=20)
rbuttonGuthaben3 = Radiobutton(root, text="30", padx = 20, variable=guthaben, value=30)

button1 = Button(root, text="Aufladen", command=checkNumber)

#Setup the grid view
setupViews()
root.mainloop()