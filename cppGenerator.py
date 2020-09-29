import os
import re

inFileText = "Replace this text with your variable names and types.\nSemicolons (;) will be removed automatically\nExample:\n\nfloat x\nfloat y\nfloat z\n\nThen run the generator with:\npython3 generator.py\nYou will be asked to input a class name"

def fixCase(key):
    key = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), key, 1)
    return key

#Create empty dictionary
varDict = {}

#Get user input for the class name
className = input("Please enter class name:\n")
print("\n")

#Read input
inFile = open("input.txt","r")
lines = inFile.readlines()

if(os.path.exists("output.txt")):
    os.remove("output.txt") #Clear output file to get rid of any old output
outFile = open("output.txt", "w+")

#Loop to read all lines from the file
try:
    for line in lines:
        line = line.strip()
        line = line.replace(";","")
        print("Read line \"" + line + "\"")

        #Convert to name and type
        splitLine = line.split(" ")
        varName = splitLine[1]
        varType = splitLine[0]
    
        #Add variable name to dictionary
        varDict[varName] = varType

except:
    #Print error to user
    print("\n\n")
    print("*******************************************************")
    print(" Input file could not be read successfully,\n did yopu save input.txt before running the generator?")
    print("*******************************************************\n")
    
    #Clear output file
    if(os.path.exists("output.txt")):
        os.remove("output.txt")
    outFile = open("output.txt", "w+")

    #Exit program
    exit()

#All vars are in the dictionary, create getters and setters

#First, to populate the header file:
# [value] [key]; - float x;
# Then getters are:
# [value] get[key](); - float getx();
# Setters are:
# void set[key]( [value] _[key] ); - void setx( float _x );
# .cpp file getters:
# [value] [className]::get[key](){ return [key]; } - float testClass::getx(){ return x; }
# .cpp file setters:
# void [className]::set[key]( [value] _[key] ){ [key] = _[key]; }

keys = varDict.keys()
#Writing header file

inFile.close()

print("Finished reading variable list, writing to output file...")
print("Writing variables for .h file")

outFile.write("For " + className + ".h:\n\n")

#Variable declarations
for key in keys:
    outFile.write(varDict[key] + " " + key + ";\n")

outFile.write("\n")

#Getters
for key in keys:
    outFile.write(varDict[key] + " get" + fixCase(key) + "();\n")

outFile.write("\n")

#Setters
for key in keys:
    outFile.write("void set" + fixCase(key) + "( " + varDict[key] + " _" + key + " );\n")

outFile.write("\n")
print("Writing variables for .cpp file")
outFile.write("For " + className + ".cpp:\n\n")

#Getters
for key in keys:
    outFile.write(varDict[key] + " " + className + "::get" + fixCase(key) + "(){ return " + key + "; }\n")

outFile.write("\n")

#Setters
for key in keys: 
    outFile.write("void " + className + "::set" + fixCase(key) + "( " + varDict[key] + " _" + key + "){ " + key + " = _" + key + "; }\n")

print("Done writing to output file, closing file...")
outFile.close()

print("Reformatting input file...")
os.remove("input.txt")
inFile = open("input.txt", "w+")

inFile.write(inFileText)
inFile.close()

print("Done!")