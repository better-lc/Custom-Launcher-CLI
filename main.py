#Modules
import parse


#Initialization
exit=0
print("")
print(" ░█████╗░██╗░░░░░")
print(" ██╔══██╗██║░░░░░")
print(" ██║░░╚═╝██║░░░░░")
print(" ██║░░██╗██║░░░░░")
print(" ╚█████╔╝███████╗")
print(" ░╚════╝░╚══════╝")
print("")
print(" Custom Launcher Python Rewrite by Aetopia.")
#Main
while exit==0:
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
        exit=1
