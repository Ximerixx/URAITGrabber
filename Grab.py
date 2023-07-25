import os
import sys
import fileinput
import time
from pprint import pprint 

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
SHIT = 0
def SDBrowser(link):
    for EveryShitPassingBy in range (10):
        #take the shit
        global SHIT 
        #count the shit
        SHIT += 1
        #if there's a puddle of shit, wait before it dissolve in air
        if SHIT >= 10:
            time.sleep(5) #let's take a nap, waiting before it vanishes
            #it vanished? NO? GOTTA WASH THAT PUDDLE!
            SHIT = 0
        #Poo
        #pooowith browser

def dBrowser(**DLink):
    #
    pass


#and there was a normal guy, trying new, fancy things
def Direct(a1Link, a1cookie):
    pass




if config['DownalodFromBrowser?'] == False : #then      ///yeah, i'm that bad///
    print("something")








print("Dowloading my ass piece by piece")