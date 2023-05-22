from random import randint


def main():
    n = get_level()
    eq = generate_equation(n)  # eq is a list with 10 elements (lists)
    s = solve(eq)
    print(f"Score: {s}")
    
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
        except ValueError:
            pass


def generate_equation(n):
    equations = []
    for i in range(10):
        if n == 1:
            start = 0
        else:
            start = 10 ** (n - 1)
        end = (10 ** n) - 1
        x = randint(start, end)
        y = randint(start, end)
        equations.append([x, y])
    return equations


def solve(eq):
    score = 10
    for i in eq:
        attempt = 3
        while attempt > 0:
            try:
                user_answer = int(input(f"{i[0]} + {i[1]} = "))
                if i[0] + i[1] != user_answer:
                    print("EEE")
                    attempt -= 1
                    if attempt < 1:
                        print(f"{i[0]} + {i[1]} = {i[0] + i[1]}")
                        score -= 1
                else:
                    break
            except ValueError:
                print("EEE")
                attempt -= 1
                if attempt < 1:
                    print(f"{i[0]} + {i[1]} = {i[0] + i[1]}")
                    score -= 1
    return score


if __name__ == "__main__":
    main()


# submit50 cs50/problems/2022/python/professor
