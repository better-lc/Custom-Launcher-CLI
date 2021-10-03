import sys
sys.path.insert(1, 'modules')
import website
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
        except:
            print("search/s <engine: Google/DuckDuckGo> <query>")
    elif cmd.lower()=="wikipedia" or cmd.lower()=="wk":
        try:
            website.wikipedia(argument)
        except:
            print("wikipedia/wk <query>")
    elif cmd.lower()=="namemc" or cmd.lower()=="n":
        try:
            website.namemc(argument)
        except:
            print("namemc/n <query>")
    elif cmd.lower()=="github" or cmd.lower()=="gh":
        try:
            website.github(argument)
        except:
            print("github/gh <user/repository")
    elif cmd.lower()=="translate" or cmd.lower()=="t":
        try:
            website.translate(argument1,argument2,argument3)
        except:
            print("translate/t <language from> <language to> <text>")
    elif cmd.lower()=="chocopackage" or cmd.lower()=="cp":
        try:
            website.chocopackagelookup(argument)
        except OSError as Error:
            print("chocopackage/cp <package name>")
                 
    else:
        print("Invaild Command/Syntax.")
