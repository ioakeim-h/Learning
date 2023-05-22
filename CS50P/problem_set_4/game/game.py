import random


def main():
    lvl = level()
    ans = get_answer(lvl)
    compare(ans, guess())


def level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass


def get_answer(lvl):
    ans = random.choice(range(1, lvl + 1))
    return ans


def guess():
    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                return g
        except ValueError:
            pass


def compare(ans, g):
    if ans > g:
        print("Too small!")
        compare(ans, guess())

    elif ans < g:
        print("Too large!")
        compare(ans, guess())

    else:
        print("Just right!")
        exit()


main()

