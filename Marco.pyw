from pynput.keyboard import Key, Listener
import os
import subprocess
from tkinter import Tk, Label, Button

Macros = []

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

#No altering outside this box

#Processes
## SoftwareOpen
## SoftwareClose
## OSCommand
## TextData

Macros.append({'Name': 'ofirefox', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files\Mozilla Firefox\\firefox.exe"})
Macros.append({'Name': 'ooutlook', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files (x86)\Microsoft Office\\root\Office16\\OUTLOOK.exe"})
Macros.append({'Name': 'ochrome', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"})
Macros.append({'Name': 'ospotify', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:/Users\Marketing\AppData\Roaming\Spotify\\Spotify.exe"})
Macros.append({'Name': 'owinscp', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files (x86)\WinSCP\\WinSCP.exe"})
Macros.append({'Name': 'ogimp', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files\GIMP 2\\bin\\gimp-2.8.exe"})
Macros.append({'Name': 'osublime', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files\Sublime Text 3\\sublime_text.exe"})
Macros.append({'Name': 'oword', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files (x86)\Microsoft Office\\root\Office16\\WINWORD.exe"})
Macros.append({'Name': 'oex', 'ProcessCommand': 'SoftwareOpen', 'Process': "C:\Program Files (x86)\Microsoft Office\\root\Office16\\EXCEL.exe"})

Macros.append({'Name': 'cfirefox', 'ProcessCommand': 'SoftwareClose', 'Process': "firefox.exe"})
Macros.append({'Name': 'coutlook', 'ProcessCommand': 'SoftwareClose', 'Process': "OUTLOOK.exe"})
Macros.append({'Name': 'cchrome', 'ProcessCommand': 'SoftwareClose', 'Process': "chrome.exe"})
Macros.append({'Name': 'cspotify', 'ProcessCommand': 'SoftwareClose', 'Process': "Spotify.exe"})
Macros.append({'Name': 'cwinscp', 'ProcessCommand': 'SoftwareClose', 'Process': "WinSCP.exe"})
Macros.append({'Name': 'cgimp', 'ProcessCommand': 'SoftwareClose', 'Process': "gimp-2.8.exe"})
Macros.append({'Name': 'csublime', 'ProcessCommand': 'SoftwareClose', 'Process': "sublime_text.exe"})
Macros.append({'Name': 'cword', 'ProcessCommand': 'SoftwareClose', 'Process': "WINWORD.exe"})
Macros.append({'Name': 'cex', 'ProcessCommand': 'SoftwareClose', 'Process': "EXCEL.exe"})

Macros.append({'Name': 'shutdown', 'ProcessCommand': 'OSCommand', 'Process': "shutdown -s"})
Macros.append({'Name': 'restart', 'ProcessCommand': 'OSCommand', 'Process': "reboot now"})

Macros.append({'Name': 'textone', 'ProcessCommand': 'TextData', 'Process': "Example Test One \n""New Line With Text"})
Macros.append({'Name': 'texttwo', 'ProcessCommand': 'TextData', 'Process': "Example Test Two \n""New Line With Text"})


#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

ArrayKeys = ["Blank"]
ArrayKeysStr = ""

def on_press(key):
    #Append each key to the list
    ArrayKeys.append(key)
    #Convert the list to a string
    KeyString = (''.join(map(str, ArrayKeys)))
    #Remove the icons from the string
    KeyString = KeyString.replace("'", '')

    # Testing
    # print (KeyString)   
    # print (ArrayKeys)

    #Clear when there are 20, help with speed and prevent crashes from overloading
    if len(ArrayKeys) == 20:
        del ArrayKeys[1]
    #Start the typing
    #The array has empty in so nothing can work unless alt is pressed
    if key == Key.alt_l:
        #Remove all items from list
        del ArrayKeys[:]

    #For each name
    for name in Macros:
        #Access from the list
        Name = name.get('Name')
        Process = name.get('Process')
        Command = name.get('ProcessCommand')

        if KeyString == Name:

            #Access list items
            if Command == "SoftwareOpen":
                OpenSoftwareFunction(Process)
            if Command == "SoftwareClose":
                CloseSoftwareFunction(Process)
            if Command == "OSCommand":
                OSCommandFunction(Process)
            if Command == "TextData":
                TextDataFunction(Process)
            del ArrayKeys[:]

#Opensoftware Function
def OpenSoftwareFunction(Process):
    subprocess.Popen(Process)

#Closesoftware Function
def CloseSoftwareFunction(Process):
    #Put into list, can then be used open and close with the same string
    #ProcessSpilt = (Process.split("\\",99)[-1])
    os.system("taskkill /f /im  %s" % Process)

#OS based Function
def OSCommandFunction(Process):
    os.system(Process)

#OS based Function
def TextDataFunction(Process):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(Process)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

#Collect events
with Listener(
       on_press=on_press
       ) as listener: 
    listener.join()

#Saved as .pyw so it can run in background
#Place in below folder to run with start up
#C:\Users\Marketing\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

# Author: Stephen Blake
# Name: Macros                               
# Dates: 31/01                               
# Ver: 1.0.0                                 
# - Get Custom Macros 
# Next Edits:
# - Box at the conor of screen to show what is being typed
# - Single line as well as software open and close separated
# - Load text from file
# - Keep log