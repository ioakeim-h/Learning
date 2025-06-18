#include <stdio.h>

8 bits = 1 byte


// Pointers - take up 8 bytes
& - address of operator (at what address is this operator?)
* - reference operator (take an address and go to it)


// print the address of n
int n = 50;
printf("%p\n", &n);


// Store addresses into variables
    int n = 50;

    // Store the address of n into p
    int *p = &n;
    printf("%p\n", p);


// Get value from an address
    int n = 50;

    // Store the address of n into p
    int *p = &n;

    // go to address and print value
    printf("%i\n", *p);


// How to read pointers
int *pX = &x;
"Integer pointer named pX is set to the address of x"

int y = *pX;
"Integer named y is set to the thing pointed to by pX"


// malloc & free
"malloc() is used to allocate memmory to a pointer.
When you call malloc, you specify the amount of memory you want to allocate (in bytes), 
and if successful, malloc returns a pointer to the first byte of the allocated space.

You should use malloc when you need to allocate memory for an object whose size you don't know until runtime. 
For example, if you're reading input from a user and you don't know how much data they're going to enter, 
you could use malloc to allocate just the right amount of memory.

Remember, when you use malloc, it's your responsibility to free the memory when you're done with it using the free function."

#include <stdlib.h>
char *ptr = malloc(strlen(s) + 1); // for string input - +1 to catch the NUL char too
int *ptr = malloc(sizeof(int) * 5); // to get memmory for 5 ints

free (ptr);

"In the context of malloc, NULL is a special value that's returned when the memory allocation request fails. 
This could happen for a few reasons, such as if there's not enough memory available to fulfill the request (e.g. too large input).
It's good practice to always check if malloc returns NULL before using the allocated memory"

int *ptr = malloc(sizeof(int) * 50); // request memory for 50 integers
if (ptr == NULL) {
    // handle the error, perhaps by exiting the program
    return 1;
}

// valgrind - check memmory usage
valgrind ./program



// scanf
"
scanf is a function in C that is used to read input from the user. It's typically used in the format scanf("%type", &variable);, 
where %type is a placeholder for the type of data you're expecting (like %d for integers, %f for floats, etc.), 
and variable is the variable where you want to store the input.

Remember, you need to use the & operator before the variable name, as scanf requires the address of the variable to store the input. 
This is because scanf modifies the variable, and in C, if you want a function to modify a variable, you need to provide the address of that variable."

//get int with scanf
int n;
scanf("%i", &n);

// get str with scanf
"When you're getting a string input, you don't need to use the & operator, because a string in C is essentially a pointer to the first character of the string."
char s[4];
scanf("%s", s); // u get a segmentation fault error when user inputs more than 4 bytes


// File I/O
FILE *file = fopen("filename.csv", "a"); // r or rb, w or wb - use r for text files (e.g. .text) and rb for binray files (e.g. images)
"fopen returns a pointer to a file"

// write to file
fprintf(file, "%s\n", something);

// close file
fclose(file);