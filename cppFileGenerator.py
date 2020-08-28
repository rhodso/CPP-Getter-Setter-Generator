import os
import re

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

if(os.path.exists((className + ".h"))):
    os.remove((className + ".h")) #Clear output file to get rid of any old output
outFile = open((className + ".h"), "w+")

#Loop to read all lines from the file
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

keys = varDict.keys()
#Writing header file

inFile.close()

print("Finished reading variable list, writing to output file...")
print("Writing .h file")


#Will write the .h file first

#Setting up the header file
outFile.write("//Header file auto-generated using CPP-Getter-Setter-Generator\n")
outFile.write("#ifndef " + className.upper() + "_H\n")
outFile.write("#define " + className.upper() + "_H\n\n")
outFile.write("//Includes\n\n\n")
outFile.write("class " + className + " {\n\tpublic:\n")

print("Writing Constructor and Destructor")

#Constructor and Destructor
outFile.write("\t\t//Constructor and Destructor\n")
outFile.write("\t\t" + className + "();\n")
outFile.write("\t\t~" + className + "();\n\n")

print("Writing Getters and Setters")

#Getters
outFile.write("\t\t//Getters and Setters\n")
for key in keys:
    outFile.write("\t\t" + varDict[key] + " get" + fixCase(key) + "();\n")

outFile.write("\n")

#Setters
for key in keys:
    outFile.write("\t\tvoid set" + fixCase(key) + "( " + varDict[key] + " _" + key + " );\n")

outFile.write("\n")

#Other methods
outFile.write("\t\t//Other methods\n\n")

print("Writing Variable Declarations")

#Private variables
outFile.write("\tprivate:\n")
outFile.write("\t\t//Variables\n")
#Variable declarations
for key in keys:
    outFile.write("\t\t" + varDict[key] + " " + key + ";\n")

outFile.write("\n")

#End of header file
outFile.write("};\n#endif")

#Tidy up
outFile.close()

print("Finished writing header file")
print("Writing source file")

#Set up for creating the source file
if(os.path.exists((className + ".cpp"))):
    os.remove((className + ".cpp")) #Clear output file to get rid of any old output
outFile = open((className + ".cpp"), "w+")

#Now to write the source file
outFile.write("//Source file auto-generated using CPP-Getter-Setter-Generator\n\n")
outFile.write("//Includes\n")
outFile.write("#include \"" + className + ".h\"\n")

print("Writing constructors and destructors")

outFile.write("\n\n//Constructor and Destructor\n")
outFile.write("" + className + "::" + className + "(){}\n")
outFile.write("" + className + "::~" + className + "(){}\n")

print("Writing Getters and setters")

outFile.write("\n//Getters and Setters\n")
#Getters
for key in keys:
    outFile.write(varDict[key] + " " + className + "::get" + fixCase(key) + "(){ return " + key + "; }\n")

outFile.write("\n")

#Setters
for key in keys: 
    outFile.write("void " + className + "::set" + fixCase(key) + "( " + varDict[key] + " _" + key + "){ " + key + " = _" + key + "; }\n")
outFile.write("\n//Other methods")

#All done writing files, time to clean up
print("Done writing to source file, closing file...")
outFile.close()

print("Reformatting input file...")
os.remove("input.txt")
inFile = open("input.txt", "w+")

inFile.write("Replace this text with your variable names and types.\nSemicolons (;) will be removed automatically\nExample:\n\nfloat x\nfloat y\nfloat z\n\nThen run the generator with:\npython3 generator.py\nYou will be asked to input a class name")
inFile.close()

print("Done!")