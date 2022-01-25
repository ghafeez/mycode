#!/usr/bin/env python3

"""Custom script to apply conditions"""
"""Code is to classify hurricane as per Saffir-Simpson scale based on user input of windspeed"""
def main():

    classification = 'Hurricane classification '    #Message to display for classification

    windspeed = float(input("What is the wind speed in km/h ")) #getting user input for windspeed

    if windspeed >= 252:                            #if condition for windspeeds above 252 km/h
        classification = classification + 'is Five as per Saffir-Simpson scale.' #printing classification
    elif windspeed >= 209:                          #if condition for windspeeds above 209 km/h
        classification = classification + 'is Four as per Saffir-Simpson scale'
    elif windspeed >= 178:                          #if condition for windspeeds above 178 km/h
        classification = classification + 'is Three as per Saffir-Simpson scale'
    elif windspeed >= 154:                          #if condition for windspeeds above 154 km/h
        classification = classification + 'is Two as per Saffir-Simpson scale'
    elif windspeed >= 119:                          #if condition for windspeeds above 119 km/h
        classification = classification + 'is One as per Saffir-Simpson scale'
    else:                                           #else this doesnt fall under any category
        classification = classification + 'does not fall under Saffir-Simpson scale, thats just windy'
    
    print(classification)

main()

