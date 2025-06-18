// Creating new data types in C
typedef struct
{
    string name;
    string number;
}
person;

// Using the new data type
person people[3];

people[0].name = "David";
people[0].number = "+1-617-496-1000";

// Recursion - a function that calls itself
/*
open in middle of book - middle index= length / 2
if number is on page
    stop
else if number < middle
    search 

*/