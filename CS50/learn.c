/*
https://manual.cs50.io/

code learn.c
make learn
./learn
*/

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    ...
}

// while loop
while (condition) {
  // code block to be executed
}


/*
for loop:

Expression 1 is executed (one time) before the execution of the code block.
Expression 2 defines the condition for executing the code block.
Expression 3 is executed (every time) after the code block has been executed.
*/ 

for (expression 1; expression 2; expression 3) {
  // code block to be executed
}




// Defining and using functions
/* 
Return Type: This indicates what type of value the function is expected to return. If the function does not return a value, use void.
Parameters: List the parameters inside parentheses, each with a type and a name. If there are no parameters, you can use void inside the parentheses.
*/

// Function declaration -- mentioned before main before functions are defined after main
int addNumbers(int a, int b);
void somefunction(void)

// Main function
int main() {
    int result = addNumbers(5, 3);
    printf("Result: %d\n", result);
    return 0;
}

// Function definition
int addNumbers(int a, int b) {
    return a + b;
}

// Function with no return value and no input
void somefunction(void) {
    ...
}



// Cycling through indices
// For example, if you have an array of length n, then using index % n ensures that your indices range from 0 to n-1, regardless of how large the index grows.
int array[5] = {10, 20, 30, 40, 50};
int index, adjusted_index;

// Let's say we're accessing the array in a loop that might go out of bounds
for (index = 0; index < 10; index++) {
    adjusted_index = index % 5; 
    printf("Element at circular index %d is: %d\n", index, array[adjusted_index]);
}
// array[adjusted_index] in the first iteration will print 10



// Extracting digits
// In the typical method of extracting digits with modulo and division by 10, the digits do indeed come out in reverse order, from last to first. 
// If you need them from first to last, an additional step is required to reverse this order after extraction.
int main() {
    int original = 4321;
    int reversed = 0;
    int digit;

    // Extract digits and reverse the order
    while (original > 0) {
        digit = original % 10; // Get the last digit
        reversed = reversed * 10 + digit; // Append digit to the reversed number
        original /= 10; // Remove the last digit from the original number
    }

    // Now extract digits from the reversed number
    while (reversed > 0) {
        digit = reversed % 10;
        printf("Digit: %d\n", digit);
        reversed /= 10;
    }

    return 0;
}
