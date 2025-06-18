// Compiling can be done with:
"
clang filename.c to output ./a.out (a is for assembler)

However, to rename the compiled file we can use CLI arguments:
clang -o desiredfilename filename.c
this will set the name of the compiled file to desiredfilename

You can then run with ./desiredfilename
"

// Compiling scripts that use third-party libraries (e.g cs50.h)
"This will result in error if the library is not mentioned during compiling - this is like pip install in python.

clan -o desiredfilename filename.c -lcs50 (l stands for library and cs50 for the cs50 library)

the 'make' compiling method is actually legit and takes care of these procedures.
"

// The entire process of compiling 
"
preprocessing - processes imported libraries (imports the actual code underneath)
compiling - converting source code into assembly code
assempling - converts assembly code to binary code (0s and 1s)
linking - combines binary code of the files involved (remember there is your code and the code imported from libraries)
"

// Debugging tools
"
1. printf
2. Dedicated debugging functions that use printf
3. Debugger - this helps with logical errors rather than syntax errors. 

How to use the debugger:
- First compile the code
- Second, set a break point
- Third, use CLI to start debugging by typing: debug50 ./filename

4. Rubber dug debugging
"


// Memmory
"
1 byte is 8 bits. Knowing this, you can understand the memmory required for C data types. For example, an int is typically 4 bytes in many systems.
Therefore: 4 * 8 = 32 bits. This means a 32-bit integer. 

In C, an int with 32 bits can represent a range of values depending on whether it is signed or unsigned:

- Signed 32-bit int: Can represent values from -2,147,483,648 to 2,147,483,647.
- Unsigned 32-bit int: Can represent values from 0 to 4,294,967,295.

Google search 32 bits max value gives us 2,147,483,647. 
"



// Using CLI args in C
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // argv[0] is always the name of the file being executed
    // argc is the argument counter
}