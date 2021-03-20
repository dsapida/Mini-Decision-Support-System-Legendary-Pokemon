import pandas as pd
import numpy as np
import time
import random

def getSample():
    #TLDR: Gets Random Sample from Dataset, Runs it through the Mini DSS as if it's a "unique" entry.
    print("\n")
    print("Getting a Random Sample from Pokemon.csv. . . \n")
    #Initializes Pokemon.csv into a Pandas Dataframe
    data = pd.read_csv('Pokemon.csv', sep=',')
    pokemon = pd.DataFrame(data)

    #Produces a random sample out of the 800 entries in Pokemon.csv
    sample = pokemon.sample()

    #Simulates waiting, even though this is pretty instantaneous because why not.
    time.sleep(3)

    #Shows the attributes of the sample
    print("Name: " + sample.iloc[0]['Name'])
    print("Type 1: " + str(sample.iloc[0]['Type 1']))
    print("Type 2: " + str(sample.iloc[0]['Type 2']))
    print("HP: " + str(sample.iloc[0]['HP']))
    print("Attack: " + str(sample.iloc[0]['Attack']))
    print("Defense: " + str(sample.iloc[0]['Defense']))
    print("Special Defense: " + str(sample.iloc[0]['Sp. Atk']))
    print("Special Attack: " + str(sample.iloc[0]['Sp. Def']))
    print("Speed: " + str(sample.iloc[0]['Speed']))
    print("Generation: " + str(sample.iloc[0]['Generation']))

    #Runs Mini DSS using that Pokemon's Attributes, if the Pokemon does not have base stats of a Standard Legendary Pokemon (Total > 579) then an error based from the tree
    #Will show up
    DSS(sample.iloc[0]['Type 1'], sample.iloc[0]['Type 2'], sample.iloc[0]['HP'], sample.iloc[0]['Attack'], sample.iloc[0]['Defense'], sample.iloc[0]['Sp. Atk'], sample.iloc[0]['Sp. Def'], sample.iloc[0]['Speed'])


def DSS(type1, type2, hp, attack, defense, spatk, spdef, speed):
    #Rules from our Decision Tree
    #Target Outputs:
        #1. Result QUALIFIES as a Balanced Legendary Pokemon
        #2. Result DOES NOT QUALIFY as a Balanced Legendary Pokemon

    #Basically based on the user input attributes, does this Pokemon qualify or not to be a balanced Legendary Pokemon
    #Our Goal is to help DESIGN a Legendary Pokemon that is NOT TOO POWERFUL (or Balanced for short)

    total = attack + defense + spatk + spdef + speed + hp
    print("\n")

    if(total <= 579):
        #Legendary = FALSE
        print("Final Result (Target Output): This does not qualify as a Balanced Legendary Pokemon!")
        print("Suggestion: A Legendary Pokemon's Stats (Attack, Defense, Sp. Atk, Sp. Def, Speed) should all add up to a Total Base Stat >= 579, Current: " + str(total))

    elif(total > 579):
        #Check if Primary Typing is Ground
        if(type1.lower() == 'ground'):
            #Legendary = TRUE
            print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
            print("Reason: Total Base Stat > 579")
            getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
        else:
            #Check if Special Attack is <= 71 or > 71
            if(spatk <= 71):
                if(attack <= 112):
                    #Legendary = TRUE
                    print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                    print("Reason: Total Base Stat > 579, Special Attack Base Stat <= 71, and Attack Base Stat <= 112")
                    getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                elif(attack > 112):
                    #Legendary = FALSE
                    print("Final Result: This does not qualify as a Balanced Legendary Pokemon!")
                    print("Suggestion: A Legendary Pokemon with a Special Attack Base Stat <= 71 MUST HAVE a Attack Base Stat <= 112")
            elif(spatk > 71):
                #Check if Primary Typing is Psychic
                if(type1.lower() == 'psychic'):
                    #Check if Attack is <= 87 or > 87
                    if(attack <= 87):
                        #Check if HP is <= 71 or > 71
                        if(hp <= 71):
                            #Legendary = FALSE
                            print("Final Result: This does not qualify as a Balanced Legendary Pokemon!")
                            print("Suggestion: A Legendary Pokemon with a primary type of 'Psychic' with a Attack Base Stat <= 87, Special Attack > 71 MUST HAVE a HP Base Stat <= 71")
                        elif(hp > 71):
                            #Legendary = TRUE
                            print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                            print("Reason: Primary Typing of Psychic with a Total Base Stat > 579, HP Base Stat > 71, Attack Base Stat <= 87, and Special Attack Base Stat > 71")
                            getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                    elif(attack > 87):
                        #Legendary = TRUE
                        print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                        print("Reason: Total Base Stat > 579, Attack Base Stat > 87, and Special Attack Base Stat > 71")
                        getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                else:
                    #If Primary Type != Psychic, Check if Speed is <= 82 or > 82
                    if(speed <= 82):
                        #Check if Primary Typing is Fire
                        if(type1.lower() == 'fire'):
                            #Legendary = TRUE
                            print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                            print("Reason: Primary Typeing of Fire with a Total Base Stat > 579, Speed Base Stat <= 82, Special Attack > 71")
                            getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                        else:
                            #If Primary Type != Fire, Check if Special Defense is <= 135 or > 135
                            if(spdef <= 135):
                                #Legendary = FALSE
                                print("Final Result: This does not qualify as a Balanced Legendary Pokemon!")
                                print("Suggestion: A Legendary Pokemon with a Speed Base Stat <= 82, Special Attack Base Stat > 71 MUST HAVE a Special Defense Base Stat > 135")
                            elif(spdef > 135):
                                #Legendary = TRUE
                                print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                                print("Reason: Total Base Stat > 579, Speed Base Stat <= 82, Special Attack > 71, and Special Defense > 135")
                                getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                    elif(speed > 82):
                        #Check if Special Defense is <= 96 or > 96
                        if(spdef > 96):
                            #Legendary = TRUE
                            print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                            print("Reason: Total Base Stat > 579, Special Defense Base Stat > 96, Speed Base Stat > 82, and Special Attack > 71")
                            getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                        elif(spdef <= 96):
                            #Check if Secondary Typing is Ice
                            if(type2.lower() == 'ice'):
                                #Legendary = TRUE
                                print("Final Result: This qualifies as a Balanced Legendary Pokemon!")
                                print("Reason: Secondary Typing of Ice with a Total Base Stat > 579, Special Defense Base Stat <= 96, Speed Base Stat > 82, and Special Attack > 71")
                                getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)
                            else:
                                #If Secondary Type != Ice, Check if Attack is <= 129 or > 129
                                if(attack > 129):
                                    #Legendary = FALSE
                                    print("Final Result: This does not qualify as a Balanced Legendary Pokemon!")
                                    print("Suggestion: A Legendary Pokemon with a Special Defense Base Stat <= 96, Speed Base Stat > 82, Special Attack > 71 MUST HAVE a Attack Base Stat <= 129")
                                elif(attack <= 129):
                                    #Check if Special Attack is <= 135 or > 135
                                    if(spatk > 135):
                                        #Legendary = FALSE
                                        print("Final Result: This does not qualify as a Balanced Legendary Pokemon!")
                                        print("Suggestion: A Legendary Pokemon with a Attack Base Stat <= 129, Special Defense Base Stat <= 96, Speed Base Stat > 82, Special Attack Base Stat > 71 MUST HAVE a Special Attack Base Stat <= 135")
                                    elif(spatk <= 135):
                                        #Legendary = TRUE
                                        print("Final Result (Target Output): This qualifies as a Balanced Legendary Pokemon!")
                                        print("Reason: Total Base Stat > 579, Special Attack Base Stat > 71 and <= 135, Attack Base Stat <= 129, Special Defense Stat <= 96, and Speed Base Stat > 82")
                                        getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed)

def getSimInfo(total, type1, type2, hp, attack, defense, spatk, spdef, speed):
    #NOTE: Repurposed, hence these other arguments are not being used, kept them in here incase of re-enabling the other commented lines in this function
    #Otherwise these arguments will not be used, other than "total"

    #Initializes the Dataset into a Pandas Dataframe
    data = pd.read_csv('Pokemon.csv', sep=',')
    pokemon = pd.DataFrame(data)

    #List of attributes to look for in the Dataframe (Dataset) (Old Variable: no longer needed due to repurpose but works still)
    #moninfo = [total, type1, type2, hp, attack, defense, spatk, spdef, speed]

    print("")
    #Gets a list of Pokemon from the Dataframe based on the total base stat
    result = pokemon['Name'].loc[pokemon['Total'].isin([total])]

    #Old Result Variable: Still works, but is commented out and replaced with the new one due to the repurpose of this function
    #result = pokemon['Name'].loc[
        #pokemon['Total'].isin(moninfo) & pokemon['Type 1'].isin(moninfo) & pokemon['Type 2'].isin(moninfo) & pokemon[
            #'HP'].isin(moninfo) & pokemon['Attack'].isin(moninfo) & pokemon['Defense'].isin(moninfo) & pokemon[
            #'Sp. Atk'].isin(moninfo) & pokemon['Sp. Def'].isin(moninfo) & pokemon['Speed'].isin(moninfo)]

    #If result returns an empty series, then there is no Pokemon that exist that have a total base stat which is based by the user input
    if(len(result) == 0):
        print("No Records of Pokemon in Pokemon.csv have that have a total base stat of " + str(total) + ". This Legendary Pokemon Design is unique!")
    else:
        #Prints out the Pokemon Name recorded in the Dataframe that have the exact same total base stat.
        #User can use this to reference similar Pokemon and analyse their allotment of base stats to improve their design or inspire future designs
        print("DSS: Here's a list of Pokemon with the same Total Base stats.")
        print("Suggestion: Use this information to see how different base stats are alloted and use them in your future designs or improve your current one!")
        print("")
        print(result)



def main():
    print("This is a Legendary Pokemon Mini DSS Prototype")
    print("-----------------------------------------------")
    print("This program allows users to help out design a Legendary Pokemon based on rules derived from a Decision Tree\n")

    print("Modes")
    print("-----")
    print("s: Sample from a Dataset")
    print("i: Input your own!")

    #User can enter s or i to either evaluate a random sample from the Pokemon.csv file or to do user input
    mode = input("Select the Mode: ")

    #User input portion
    if(mode == 'i'):
        print("\n")
        print("Please enter the following Type(s) and Base Stats")

        type1 = input("Type 1: ")
        type2 = input("Type 2: ")
        if(type2 == ""):
            type2 = np.nan
        hp = int(input("HP: "))
        attack = int(input("Attack: "))
        defense = int(input("Defense: "))
        spatk = int(input("Special Attack: "))
        spdef = int(input("Special Defense: "))
        speed = int(input("Speed: "))


        #Conducts the mini DSS after all attributes have been inputted
        DSS(type1, type2, hp, attack, defense, spatk, spdef, speed)

    elif(mode == 's'):
        #Get random sample and uses DSS to evaluate it
        getSample()
    else:
        #Invalid input
        print("not valid")
        exit(1)

if __name__ == '__main__':
    main()