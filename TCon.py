# App: Temperature Unit Convertor
# Developed Date: 11th July 2021
# Version: 1.0.0
# Developer: HMandro

## Modules
import os
import time

## Base Loop
os.system('cls' if os.name == 'nt' else 'clear')
Loop = True
while Loop == True:

## Input
    print("Celsius(1), Fahrenheit(2), Kelvin(3), Exit(4)\n")

    ## From Loop
    LoFM = True
    while LoFM == True:

        FM = int(input("\nConvert from: "))

        if (FM == 4):
            exit()

        elif (FM > 0 and FM < 5):
            break

        elif (FM < 1 and FM > 5):
            LoFM == True


    ## To Loop        
    LoTO = True
    while LoTO == True:

        TO = int(input("\nConvert to: "))

        if (TO == 4):
            exit()

        elif (TO > 0 and TO < 5):
            break

        elif (TO < 1 and TO > 5):
            LoTO == True


    T = float(input("\nEnter the number: "))

## Process
    os.system('cls' if os.name == 'nt' else 'clear')

    ## Celsius
    if (FM == 1 and TO == 2):
        F = (T * 9/5) + 32
        print(f"{T}°C = {F}°F\n")
        time.sleep(3)

    elif (FM == 1 and TO == 3):
        K =  T + 273
        print(f"{T}°C = {K}°K\n")
        time.sleep(3)


    ## Fahrenheit    
    elif (FM == 2 and TO == 1):
        C = (T - 32) * 5/9
        print(f"{T}°F = {C}°C\n")
        time.sleep(3)

    elif (FM == 2 and TO == 3):
        K = (T - 32) * 5/9 + 273
        print(f"{T}°F = {K}°K\n")
        time.sleep(3)


    ## Kelvin    
    elif (FM == 3 and TO == 1):
        C =  T - 273
        print(f"{T}°K = {C}°C\n")
        time.sleep(3)

    elif (FM == 3 and TO == 2):
        F = (T - 273) * 9/5 + 32
        print(f"{T}°K = {F}°F\n")
        time.sleep(3)