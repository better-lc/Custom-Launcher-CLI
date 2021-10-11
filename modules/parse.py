import sys
import website
import platform
import files
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
    if cmd.lower()=="help":
        print("")
        print("Web/Internet Related")
        print("-----------------------------")
        print("search/s <engine: Google/DuckDuckGo/DuckDuckGoLite/QWant/Brave> <query> => Search using your preferred search engine.")
        print("wikipedia/wk <query> => Look up something on Wikipedia.")
        print("namemc/n <query> => Lookup something on NameMC")
        print("github/gh <user/repository => Lookup a user or repository on GitHub.")
        print("translate/t <language from> <language to> <text> => Translate text from one language to another.")
        print("chocopackage/cp <package name> => Lookup for chocolatey packages.")
        print("-----------------------------")
        print("")
        print("Files/Folders Related")
        print("-----------------------------")
        print("downloads/dl => Open up your Downloads folder.")
        print("videos/v => Open up your Videos folder.")
        print("windowsapps/wr => Open up your Windows Apps folder.")
        print("resourcepacks/rp => Open up your Minecraft resource packs folder.")
        print("screenshots/sc => Open up your Minecraft screenshots folder.")
        print("homedrive/hd/c => Open up the C:\ drive folder.")
        print("-----------------------------")
        Finish=False
    elif cmd.lower()=="chorogon":
        print("An Easter Egg for Miss Kobayashi's Dragon Maid. [0w0]")
        Finish=False
        
    #Web/Internet
        
    elif cmd.lower()=="search" or cmd.lower()=="s":
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
            Finish=False
            
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
            Finish=False
            
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
            
    #Files
            
    elif cmd.lower()=="downloads" or cmd.lower()=="dl":
        try:
            if platform.system() == 'Windows':
                files.UserFolder("Downloads")
                Finish=True
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
            
    elif cmd.lower()=="videos" or cmd.lower()=="v" :
        try:
            if platform.system() == 'Windows':
                files.UserFolder("Videos")
                Finish=True
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
            
    elif cmd.lower()=="sendto" or cmd.lower()=="st":
        try:
            if platform.system() == 'Windows':
                files.App("SendTo")
                Finish=True
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
            
    elif cmd.lower()=="windowsapps" or cmd.lower()=="wr":
        try:
            if platform.system() == 'Windows':
                files.App("WR")
                Finish=True
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
            
    elif cmd.lower()=="resourcepacks" or cmd.lower()=="rp" :
        try:
            if platform.system() == 'Windows':
                files.Minecraft("RP")
                Finish=True
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
            
    elif cmd.lower()=="screenshots" or cmd.lower()=="sc":
        try:
            if platform.system() == 'Windows':
                files.Minecraft("RP")
                Finish=True  
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
            
    elif cmd.lower()=="homedrive" or cmd.lower()=="hd" or cmd.lower()=="c":
        try:
            if platform.system() == 'Windows':
                files.Drive()
                Finish=True  
            else:
                print("This command is only supported on Windows!")
                Finish=False
        except:
            Finish=False
    else:
        print("Invaild Command/Syntax.")
        Finish=False        
    if Finish==True:
        sys.exit()
         
