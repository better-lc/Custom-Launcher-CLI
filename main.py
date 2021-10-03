#Modules
import sys
sys.path.insert(1, 'modules')
import parse


#Initialization
Exit=False
print("")
print(" ░█████╗░██╗░░░░░")
print(" ██╔══██╗██║░░░░░")
print(" ██║░░╚═╝██║░░░░░")
print(" ██║░░██╗██║░░░░░")
print(" ╚█████╔╝███████╗")
print(" ░╚════╝░╚══════╝")
print("")
print("Custom Launcher Python Rewrite by Aetopia.")
#Main
while Exit==False:
    print("")
    command=input("Command > ")
    if command=="help":
        print("")
        print("Web/Internet Related")
        print("-----------------------------")
        print("search/s <engine: Google/DuckDuckGo/DuckDuckGoLite/QWant/Brave> <query>")
        print("wikipedia/wk <query>")
        print("namemc/n <query>")
        print("github/gh <user/repository")
        print("translate/t <language from> <language to> <text>")
        print("chocopackage/cp <package name>")
        print("-----------------------------")
    else:
        parse.input(command)
