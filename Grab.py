import os
import sys
import fileinput
import time
from pprint import pprint 
import webbrowser
import json 



print("getting everything we should know from config file");
with open('config.json') as dict:
    config = json.load(dict)
#print(config['BookID']) #test shit

print(config['LastPage'])
#and now the pat i'm ashamed of 
#GENERATING LINKS
GeneraliusLink = config['GeneralURL'] + config['BookID']
print(GeneraliusLink) #book's generalazied link
GeneralisimuxLinks =  [] #fuck me sideways
shit=0
for shiT in range (config['LastPage']+1):
        
        shit += 1 #shit ++ bishes
        GeneralisimuxLinks.append(GeneraliusLink+"/"+str(shit))
#print(GeneralisimuxLinks) #fisting purposes only
with open("links.json", "w") as fp:
    json.dump(GeneralisimuxLinks, fp)  # encode dick into JSON
print("Done writing GibeIriesh")
#well technically it isn't a valid JSON but fuck you sideways


#"In the hellfire of twisted metal was one guy..."
        #глобаль щит равен нулю сука
        #НУЛЮ Я СКАЗАЛ
#SHIT = 0
#def SDBrowser(dodolink):
#    print("sdb")
#    for EveryShitPassingBy in range (10):
#        #take the shit
#        global SHIT 
#        #count the shit
#        SHIT += 1
#        print("sdb2")
#        #if there's a puddle of shit, wait before it dissolve in air
#        if SHIT >= 10:
#            time.sleep(5) #let's take a nap, waiting before it vanishes
#            #it vanished? NO? GOTTA WASH THAT PUDDLE!
#            SHIT = 0
#            print("sdb3")
#        
#        #Poo
#        #pooowith browser
#        print(dodolink)

SHIT=0
count = 0
def dBrowser(self):
    #fro every list entry call tre download er
    for everyshit in GeneralisimuxLinks:
        for EveryShitPassingBy in range (10):
            #take the shit
            global SHIT 
            #count the shit
            global count
            
            SHIT += 1
            #if there's a puddle of shit, wait before it dissolve in air
            if SHIT >= 10:
                time.sleep(5) #let's take a nap, waiting before it vanishes
                #it vanished? NO? GOTTA WASH THAT PUDDLE!
                SHIT = 0
            #Poo
            #pooowith browser
            print(GeneralisimuxLinks[count])
            webbrowser.open(GeneralisimuxLinks[count])
            count += 1
    


import requests
#and there was a normal guy, trying new, fancy things
def Direct():
    
    #setting things up
    for everyelement in GeneralisimuxLinks:
        global count
        count = 0
        #payload to get request
        #taking it from payload.json
        for element in range(config['LastPage']):
            payload = []
            with open('payload.json') as dict:
                payload = json.load(dict)
            url = GeneralisimuxLinks[count]
            count += 1
            request = requests.get(url, params=payload)
            CurrMane = "page_000"+str(count)+".svg"
            with open(CurrMane, "wb") as f:
                f.write(request.content)
            if config['DeMark'] == True:
                pass
                #DeMark(CurrMane)
        


#needed to fix_LOL

#def DeMark(filename):
#    with open(filename, 'r') as f:
#        lines = f.readlines()
#        #find index of line to remove
#        for index, line in enumerate(lines):
#            template = config['TemplateToRemove']
#            #'''<text x="10" y="666" font-size="13" font-family="Arial" fill="#cccccc">https://urait.ru</text>'''
#            if template in line:
#                #remove line
#                print("Found one!")
#                #lines=[line.replace( '''font-size="13" font-family="Arial" fill="#cccccc">https://urait.ru</text></svg>''', "</svg>" ) for line in lines]
#                lines=line.replace( template, '''</svg>''')
#                #lines.pop(index)
#            #lines.append(index, "</svg>")   g>''', "</svg>" )
#            break
#    #writeew file   
#    with open(filename, 'w') as f:
#        f.write(''.join(lines))






if config['DownalodFromBrowser?'] == False : #then      ///yeah, i'm that bad///
    Direct()
elif config['DownalodFromBrowser?'] == True: #go fuck
    dBrowser(GeneralisimuxLinks)
else:
    Exception("Mode wasn't specified") 








print("Dowloading my ass piece by piece finished")