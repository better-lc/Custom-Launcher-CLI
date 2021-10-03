import webbrowser
import platform

def search(engine, query):
    if engine.lower()=="google" or engine.lower()=="g":
        url='https://www.google.com/search?q='
    if engine.lower()=="emoji":
        url='https://emojipedia.org/search/?q='
    if engine.lower()=="wikipedia":
        url='https://wikipedia.org/w/index.php?search='
    if engine.lower()=="duckduckgo" or engine.lower()=="ddg":
        url='https://www.duckduckgo.com/?t=ffab&q='
    if engine.lower()=="duckduckgolite" or engine.lower()=="ddgl":
        url='https://lite.duckduckgo.com/lite/?q='
    if engine.lower()=="qwant" or engine.lower()=="qw":
        url='https://www.qwant.com/?q='
    if engine.lower()=="brave" or engine.lower()=="b":
        url='https://search.brave.com/search?q='
    query=query.replace(" ", "+")
    webbrowser.open(url+query)
        
def namemc(query):
    webbrowser.open('https://namemc.com/search?q='+query)

def github(username):
    webbrowser.open('https://github.com/'+username)

def translate(langfrom,langto,text):
    text=text.replace(" ", "+")
    webbrowser.open('https://translate.google.com/?sl='+langfrom+'from&tl='+langto+'&text='+text)
                    
def chocopackagelookup(package):
        package=package.replace(" ","+")
        webbrowser.open('https://community.chocolatey.org/packages?q='+package)
