#Modules
import sys
import os
import platform
sys.path.insert(1, 'modules')
import parse

#Title
Version="v0.1 Alpha"
if platform.system()=="Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Custom Launcher "+ Version)
else:
    sys.stdout.write("Custom Launcher "+Version)

#Initialization
Exit=False
print("")
print("")
print(" ░█████╗░██╗░░░░░")
print(" ██╔══██╗██║░░░░░")
print(" ██║░░╚═╝██║░░░░░")
print(" ██║░░██╗██║░░░░░")
print(" ╚█████╔╝███████╗")
print(" ░╚════╝░╚══════╝")
print("")
print("Version:",Version)
print("Custom Launcher Python Rewrite by Aetopia.")
#Main
while Exit==False:
    print("")
    command=input("Command > ")
    parse.input(command)
