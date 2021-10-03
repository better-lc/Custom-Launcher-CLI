import sys
import website
import platform
Finish=False
def input(command):
#Input Parsing
    try:
        cmd, argument1, argument2, argument3=command.split(" ", 3)
    except:    
        try:
            cmd, argument1, argument2=command.split(" ",2)
        except:   
            try:
                cmd, argument=command.split(" ",1)
            except:
                cmd=command
    #Websites   
    if cmd.lower()=="search" or cmd.lower()=="s":
        try:
            website.search(argument1, argument2)
            Finish=True
        except:
            print("search/s <engine: Google/DuckDuckGo/DuckDuckGoLite/QWant/Brave> <query>")
            Finish=False
    elif cmd.lower()=="wikipedia" or cmd.lower()=="wk":
        try:
            website.wikipedia(argument)
            Finish=True
        except:
            print("wikipedia/wk <query>")
    elif cmd.lower()=="namemc" or cmd.lower()=="n":
        try:
            website.namemc(argument)
            Finish=True
        except:
            print("namemc/n <query>")
            Finish=False
    elif cmd.lower()=="github" or cmd.lower()=="gh":
        try:
            website.github(argument)
            Finish=True
        except:
            print("github/gh <user/repository")
    elif cmd.lower()=="translate" or cmd.lower()=="t":
        try:
            website.translate(argument1,argument2,argument3)
            Finish=True
        except:
            print("translate/t <language from> <language to> <text>")
            Finish=False
    elif cmd.lower()=="chocopackage" or cmd.lower()=="cp":
        try:
            if platform.system() == 'Windows':
                website.chocopackagelookup(argument)
                Finish=True
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            print("chocopackage/cp <package name>")
            Finish=False   
    else:
        print("Invaild Command/Syntax.")
        Finish=False

    if Finish==True:
        sys.exit()
         
