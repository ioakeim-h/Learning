#include <cs50.h>
#include <stdio.h>

int get_height();
void design(int height);

int main()
{
    int h = get_height();
    design(h);
}


int get_height()
{
    while (true){
        int height = get_int("Height: ");
        if (height > 0 && height < 9){
            return height;
        }
    }
}


void design(int height)
{
    int units = height;
    int used = 1;

    while (units > used) {
        for (int side_space = (height - 1); side_space > 0; side_space--){
            printf(" ");
        }
        height--;

        for (int blocks = units - (units - used); blocks > 0; blocks--) {
            printf("#");
        }

        printf("  ");

        for (int blocks = units - (units - used); blocks > 0; blocks--) {
            printf("#");
        }
        used++;

        printf("\n");
    }
}





