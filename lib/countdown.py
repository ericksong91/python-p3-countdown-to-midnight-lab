import time


def countdown(t):
    for x in reversed(range(1, t + 1)):
        print(f"{x} SECOND(S)!")

    print("HAPPY NEW YEAR!")


def countdown_with_sleep(t):
    for x in reversed(range(1, t + 1)):
        print(f"{x} SECOND(S)!")
        time.sleep(1)

    print("HAPPY NEW YEAR!")


countdown_with_sleep(5)
