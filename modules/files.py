#Modules
import os
import subprocess

def Explorer(Folder):
    subprocess.Popen(["explorer.exe", Folder])

def UserFolder(Folder):
    if Folder=="Downloads":
        Path=os.environ['USERPROFILE']+"\\Downloads"
    elif Folder=="Videos":
        Path=os.environ['USERPROFILE']+"\\Videos"    
    Explorer(Path)
    
def App(Folder):
    if Folder=="SendTo":
        Path=os.environ['APPDATA']+"\\Microsoft\Windows\SendTo"
    elif Folder=="WR":
        Path=os.environ['LOCALAPPDATA']+"\\Microsoft\WindowsApps"
    Explorer(Path)    

def Minecraft(Folder):
    if Folder=="RP":
        Path=os.environ['APPDATA']+"\\.minecraft\\resourcepacks"
    elif Folder=="SC":
        Path=os.environ['APPDATA']+"\\.minecraft\\screenshots"
    Explorer(Path)

def Drive():
    Path="C:\\"
    Explorer(Path)
