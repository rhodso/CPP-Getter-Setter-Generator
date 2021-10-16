# CPP-Getter-Setter-Generator
Generates code for C++ souce and header files. 
Why write 10 mins of code when you can spend 2 hours automating it and never needing to do it again?

# How it works:
Add a list of variable types and names, in any order, to the input file (input.txt)

Some special lines you can use:  
Use returnType methodName() to create a blank method with a return type  
Add #include <file> to add an include to the auto-generated header file, also works with #include "file"  
 
Semicolons (;) will be removed automatically  
Please note that #include generation and method generation are only available when using the file generator  
 
Example input: 
```
#include "exampleInclude.h"
float x
float y
float z
void doSomething()
float doSomethingElse()
void voidTestMethod(float testInput)
float testMethod(float testInput)
float testMethod(float testInput, int testInput2)
```
This input produces the testClass.h and testClass.cpp files when using the file generator. 

Using the input:  
```
float x  
float y  
float z  
```
produces the output shown in output.txt 
 
# Running the generator: 
Run the generator of your choice with:  
python3 cppGenerator.py or python3 cppFileGenerator.py  
You will be asked to input a class name, then the program will generate output based on where it's up to  
The program will let you know when it's done  
