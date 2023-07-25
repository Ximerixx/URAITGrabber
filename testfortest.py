#from time import sleep
import time



SHIT = 0


def SortingShit(siht):
    for EveryShitPassingBy in range (10):
        #take the shit
        global SHIT 
        #глобаль щит равен нулю сука
        #НУЛЮ Я СКАЗАЛ

        #count the shit
        SHIT += 1
        #if there's a puddle of shit, wait before it dissolve in air
        if SHIT >= 10:
            time.sleep(5) #let's take a nap, waiting before it vanishes
            #it vanished? NO? GOTTA WASH THAT PUDDLE!
            SHIT = 0
        #Poo
        print("poo"+"     "+str(SHIT)+ "    with othet shit ${siht}")




for dodo in range (0, 100):
    SortingShit(dodo)