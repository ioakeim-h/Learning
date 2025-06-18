#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

void validate_key(string key);
void cipher_text(string key);

int main(int argc, string argv[])
{
    if (2 != argc)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    validate_key(argv[1]);
    cipher_text(argv[1]);
}

void validate_key(string key)
{
    // Get key length the fun way
    int length = 0;
    for (int i = 0; key[i] != '\0'; i++)
    {
        length++;
    }

    // Explore char type 
    int non_alpha = 0;
    // for (int i = 0; i < length; i++)
    // {
    //     key[i] = toupper(key[i]);

    //     // Not an alphabetical char
    //     if ((65 > key[i] || 90 < key[i]))
    //     {
    //         non_alpha = 1;
    //         break;
    //     }
    // }

    // Locate duplicate chars
    int repeats = 0;
    for (int i = 0; i < length; i++)
    {
        if (repeats > 1)
            break;
        char letter = toupper(key[i]);
        
        for (int j = 0; j < length; j++)
        {
            if (letter == toupper(key[j]))
                repeats++;
        }
    }
    // loop over the entire key
    // while looping use an if condition to see if i is in the array
    // 

    // duplicate_score should match uniqueness_score to suggest unique chars
    int uniqueness_score = 0;
    for (int i = 'A'; i < 'Z' + 1; i++)
    {
        uniqueness_score += i;
    }

    if (26 != length || 0 != non_alpha || uniqueness_score != duplicate_score)
    {
        printf("Key must contain 26 unique alphabetical characters\n");
        exit(1);
    }
}

void cipher_text(string key)
{
    string text = get_string("plaintext: ");

    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                text[i] = key[text[i] - 'A'];
            }
            else
            {
                text[i] = tolower(key[text[i] - 'a']);
            }
        }

    }
    printf("ciphertext: %s\n", text);
}
