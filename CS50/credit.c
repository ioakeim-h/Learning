#include <cs50.h>
#include <math.h>
#include <stdio.h>


int main()
{
    long card_number = get_long("Number: ");
    validate(card_number);
}

validate(long number)
{
    int length = validate_length(number);
}



int validate_length(n)
{
    if (n == 0)
    {
        int l = 1;
    }
    else
    {
        int l = floor(log10(fabs(n))) + 1 // fabs to handle negative numbers
        printf("%i\n", l);
    }
}